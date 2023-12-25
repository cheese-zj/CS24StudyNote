import json
import logging
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import pandas as pd
import sup
from sqlalchemy import text

def generate_random_date():
    # 随机生成起始和结束日期
    start_year = random.randint(2022, 2023)
    start_month = random.randint(1, 12)
    start_day = random.randint(1, 28)  # 使用28来避免月份天数问题
    start_date = datetime(start_year, start_month, start_day).date()
    end_date = start_date + timedelta(days=random.randint(1, 30))
    return start_date, end_date


def get_user_input(engine):
    stock_id = input("Enter stock ID (e.g., sh600000): ")
    if not stock_id in sup.get_ids(engine):
        print("Invalid stock ID.")
        return None, None, None

    start_date = input("Enter start date (YYYY-MM-DD) or 'random': ")
    if start_date.lower() == 'random':
        start_date, end_date = generate_random_date()
    else:
        start_date = sup.validate_date(start_date)
        if not start_date:
            print("Invalid start date.")
            return None, None, None
        end_date = sup.validate_date(input("Enter end date (YYYY-MM-DD): "))
        if not end_date:
            print("Invalid end date.")
            return None, None, None
        if end_date <= start_date:
            print("End date must be after start date.")
            return None, None, None

    return stock_id, start_date, end_date

def insert_data(engine, table_name, stock_id, start_date, end_date):
    operation_type = "Update"
    
    # 构造要插入的数据字典
    data_to_insert = {
        'stock_id': stock_id,
        'start_date': start_date.strftime("%Y-%m-%d"),
        'end_date': end_date.strftime("%Y-%m-%d"),
        'operation_type': operation_type
    }

    # 使用 text() 函数包装 SQL 插入语句
    insert_query = text(f"INSERT INTO {table_name} (stock_id, start_date, end_date, operation_type) VALUES (:stock_id, :start_date, :end_date, :operation_type)")

    with engine.connect() as connection:
        # 执行 SQL 语句，将字典作为参数传递
        connection.execute(insert_query, data_to_insert)
        connection.commit()

    return


def Insert_task():
    engine_Task = sup.create_db_engine('Config/Task_db.json')
    engine_Stock_sh = sup.create_db_engine('Config/Stock_sh_db.json')
    if engine_Task is None:
        return

    stock_id, start_date, end_date = get_user_input(engine_Stock_sh)
    if stock_id and start_date and end_date:
        insert_data(engine_Task, "User_tasks", stock_id, start_date, end_date)
        print("Data inserted successfully.")
    return



