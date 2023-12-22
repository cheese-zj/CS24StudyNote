import akshare as ak

import mysql.connector

import pandas as pd

from sqlalchemy import create_engine ,text ,MetaData, Table

import json

from datetime import datetime, timedelta ,date

from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import sup

import traceback

import time

def Update_to_db_direct(engine, item):
    try:
        # 执行删除操作
        with engine.begin() as conn:
            start_date_formatted = sup.format_date(item[1], 'no_hyphen')
            end_date_formatted = sup.format_date(item[2], 'no_hyphen')

            stock_data = ak.stock_zh_a_hist_tx(symbol=f"{item[0]}", start_date=start_date_formatted, end_date=end_date_formatted)
            stock_data['stock_id'] = item[0]
            main_table_name = f"A_share{sup.hash_id_to_digit(item[0])}"

            delete_query = text(f"""
            DELETE FROM {main_table_name}
            WHERE stock_id = :stock_id AND date BETWEEN :start_date AND :end_date
            """)
            conn.execute(delete_query, {'stock_id': item[0], 'start_date': start_date_formatted, 'end_date': end_date_formatted})

        # 执行插入操作
        with engine.begin() as conn:
            stock_data.to_sql(name=main_table_name, con=engine, if_exists='append', index=False, method='multi', chunksize=20)

            # 数据验证
            verify_query = text(f"""
            SELECT COUNT(*) FROM {main_table_name}
            WHERE stock_id = :stock_id AND date BETWEEN :start_date AND :end_date
            """)
            result = conn.execute(verify_query, {'stock_id': item[0], 'start_date': start_date_formatted, 'end_date': end_date_formatted}).fetchone()
            if result[0] == len(stock_data):
                print(f"数据插入验证成功，表 {main_table_name} 中新插入了 {result[0]} 条记录。")
            else:
                print(f"数据插入验证失败，期望更新 {len(stock_data)} 条，实际更新 {result[0]} 条。")

    except Exception as e:
        print(f"在更新数据库时发生错误: {e}")
        traceback.print_exc()


def create_db_engine(config_file):
    try:
        with open(config_file, 'r') as json_file:
            db_info = json.load(json_file)

        database_url = f"{db_info['dialect']}://{db_info['username']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"
        engine = create_engine(database_url)
        return engine
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def read_Tasks(engine, table_name):
    metadata = MetaData()
    t = Table(f'{table_name}', metadata, autoload_with=engine)

    data = []
    with engine.connect() as connection:
        result = connection.execute(t.select())
        for row in result:
            data.append(row)

    return data

def process_group(db_config_file, group):
    engine = create_db_engine(db_config_file)
    for item in group:
        try:
            Update_to_db_direct(engine, item)
        except Exception as e:
            print(f"处理组 {group} 中的项 {item} 时出现错误: {e}")

def main():
    db_config_stock_sh = 'Config/Stock_sh_db.json'
    db_config_task = 'Config/Task_db.json'

    engine_Task = create_db_engine(db_config_task)
    items = read_Tasks(engine_Task, "User_tasks")
    grouped_items = sup.group_items_by_hash_id(items)

    with multiprocessing.Pool(processes=5) as pool:
        results = []
        for group in grouped_items:
            result = pool.apply_async(process_group, args=(db_config_stock_sh, group))
            results.append(result)
        pool.close()
        pool.join()

        for result in results:
            result.get()

if __name__ == "__main__":
    main()

