import akshare as ak

import mysql.connector
from mysql.connector import Error

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import MetaData, Table

import json

from datetime import datetime, timedelta ,date

from concurrent.futures import ThreadPoolExecutor


def hash_id_to_digit(id_str):
    # 计算id的字符总和
    # Calculate the sum of characters of id 
    total = sum(ord(char) for char in id_str)

    # 取余数以映射到0-9
    # Take the remainder to map to 0-9
    digit = total % 10

    return digit

def Update_to_db_direct(engine, item):
    try:
        with engine.begin() as conn:
            print(f"Fetching data for stock: {item[0]}")
            stock_data = ak.stock_zh_a_hist_tx(symbol=f"{item[0]}", start_date=format_date(item[1], 'no_hyphen'), end_date=format_date(item[2], 'no_hyphen'))

            print("Processing data")
            stock_data['date'] = pd.to_datetime(stock_data['date']).dt.date
            stock_data['stock_id'] = item[0]

            main_table_name = f"A_share{hash_id_to_digit(item[0])}"

            print(f"Deleting existing data from {main_table_name}")
            delete_query = text(f"""
            DELETE FROM {main_table_name}
            WHERE stock_id = :stock_id AND date BETWEEN :start_date AND :end_date
            """)
            conn.execute(delete_query, {'stock_id': item[0], 'start_date': format_date(item[1], 'no_hyphen'), 'end_date': format_date(item[2], 'no_hyphen')})

            # print(f"Inserting new data into {main_table_name}")
            # # 设置 chunksize 参数为例如 1000
            # stock_data.to_sql(name=main_table_name, con=engine, if_exists='append', index=False, method='multi', chunksize=1000)

            # print("Data written to database successfully.")

    except Exception as e:
        print(f"An error occurred while writing to the database: {e}")

def format_date(d, fmt_type):
    """
    将 datetime.date 对象格式化为不同的字符串格式。

    :param d: datetime.date 对象
    :param fmt_type: 格式类型，'hyphen' 为 'YYYY-MM-DD'，'no_hyphen' 为 'YYYYMMDD'
    :return: 格式化后的日期字符串
    """
    if not isinstance(d, date):
        return "Invalid input: The input must be a datetime.date object."

    if fmt_type == 'hyphen':
        # 格式化为 'YYYY-MM-DD'
        return d.strftime('%Y-%m-%d')
    elif fmt_type == 'no_hyphen':
        # 格式化为 'YYYYMMDD'
        return d.strftime('%Y%m%d')
    else:
        return "Invalid format type: Choose 'hyphen' or 'no_hyphen'."


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

    items = read_Tasks(engine_Task,"User_tasks")
    print(f"Tasks read from database: {items}")

    # Using ThreadPoolExecutor to process items in parallel
    with ThreadPoolExecutor(max_workers=1) as executor:  # Changed to 1 for single-threaded execution
        futures = [executor.submit(Update_to_db_direct, engine_Stock_sh, item) for item in items]

        # Optionally, handle the results of the futures if necessary
        for future in futures:
            try:
                result = future.result()  # This blocks until the future is done
                print(f"Future result: {result}")  # Handle the result as needed
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__=="__main__":
	main()


