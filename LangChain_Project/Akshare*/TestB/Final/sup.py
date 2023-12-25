import akshare as ak
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, text, MetaData, Table
import json
from datetime import datetime, timedelta, date
from concurrent.futures import ThreadPoolExecutor
import sup
import traceback
import time
import logging
import os

def read_Tasks(engine, table_name):
    metadata = MetaData()
    t = Table(f'{table_name}', metadata, autoload_with=engine)

    data = []
    with engine.connect() as connection:
        result = connection.execute(t.select())
        for row in result:
            data.append(row)

    return data

def hash_id_to_digit(id_str):
    # 计算id的字符总和
    # Calculate the sum of characters of id 
    total = sum(ord(char) for char in id_str)

    # 取余数以映射到0-9
    # Take the remainder to map to 0-9
    digit = total % 10

    return digit

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


def group_items_by_hash_id(items, groups=5):
    # 创建一个字典，每个键对应一组
    grouped_items = {i: [] for i in range(groups)}

    for item in items:
        # 根据 hash_id_to_digit 的结果对项目进行分组
        group_key = hash_id_to_digit(item[0]) // 2  # 0-9 的 hash 结果分成 5 组
        grouped_items[group_key].append(item)

    return list(grouped_items.values())

def print_group(grouped_items):
    '''
    Print the grouped information!
    '''
    i = 0
    while i < len(grouped_items):
        print(f"Group{i+1}:")
        for x in grouped_items[i]:
            print(x,f" Table : A_share{hash_id_to_digit(x[0])}")
        print("\n\n")
        i += 1
        
    return

def create_db_engine(config_file):
    try:
        with open(config_file, 'r') as json_file:
            db_info = json.load(json_file)

        database_url = f"{db_info['dialect']}://{db_info['username']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"
        engine = create_engine(database_url)
        return engine
    except Exception as e:
        logging.error(f"An error occurred creating the database engine: {e}")
        return None


def get_ids(engine):
    query = "SELECT id FROM stock_ids"  # 替换 your_table_name 为您的表名
    df = pd.read_sql(query, engine)

    # 将 'id' 列转换为列表
    id_list = df['id'].tolist()
    return id_list

def validate_date(input_date):
    # 验证日期格式是否正确
    try:
        return datetime.strptime(input_date, "%Y-%m-%d").date()
    except ValueError:
        return None


