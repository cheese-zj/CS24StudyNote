import akshare as ak

import mysql.connector

import pandas as pd

from sqlalchemy import create_engine ,text ,MetaData, Table

import json

from datetime import datetime, timedelta ,date

from concurrent.futures import ThreadPoolExecutor

import sup

import traceback

import time

def Update_to_db_direct(engine, item):
    try:
        # 执行删除操作
        with engine.begin() as conn:
            print(f"Processing item: {item}")

            start_date_formatted = sup.format_date(item[1], 'no_hyphen')

            end_date_formatted = sup.format_date(item[2], 'no_hyphen')
            print(f"Formatted start date: {start_date_formatted}, end date: {end_date_formatted}")

            stock_data = ak.stock_zh_a_hist_tx(symbol=f"{item[0]}", start_date=start_date_formatted, end_date=end_date_formatted)


            stock_data['stock_id'] = item[0]

            main_table_name = f"A_share{sup.hash_id_to_digit(item[0])}"
            print(f"Main table name: {main_table_name}")

            delete_query = text(f"""
            DELETE FROM {main_table_name}
            WHERE stock_id = :stock_id AND date BETWEEN :start_date AND :end_date
            """)
            conn.execute(delete_query, {'stock_id': item[0], 'start_date': start_date_formatted, 'end_date': end_date_formatted})
            print(f"Deleted existing records from {main_table_name} for stock ID {item[0]} between {start_date_formatted} and {end_date_formatted}")

        #执行插入操作
        with engine.begin() as conn:
            print(f"Inserting new records into {main_table_name}")
            stock_data.to_sql(name=main_table_name, con=engine, if_exists='append', index=False, method='multi', chunksize=20)
            print(f"Inserted new records into {main_table_name}")

    except Exception as e:
        print(f"An error occurred while writing to the database: {e}")
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


def main():
    engine_Stock_sh = create_db_engine('Config/Stock_sh_db.json')
    engine_Task = create_db_engine('Config/Task_db.json')

    items = read_Tasks(engine_Task, "User_tasks")

    #将 items 分组
    grouped_items = sup.group_items_by_hash_id(items)
    print(grouped_items)

    #使用 ThreadPoolExecutor 处理分组的 items
    with ThreadPoolExecutor(max_workers=5) as executor:
        for group in grouped_items:
            executor.submit(process_group, engine_Stock_sh, group)
    return
    

def process_group(engine, group):
    for item in group:
        try:
            Update_to_db_direct(engine, item)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__=="__main__":
    main()



    
