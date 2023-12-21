import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import random

def insert_data(cursor, table_name, stock_ids):
    for stock_id in stock_ids:
        # 随机生成起始日期
        start_year = random.randint(2022, 2023)
        start_month = random.randint(1, 12)
        start_day = random.randint(1, 28)  # 使用28来避免月份天数问题
        start_date = datetime(start_year, start_month, start_day).date()

        # 随机生成结束日期，确保结束日期在开始日期之后
        end_date = start_date + timedelta(days=random.randint(1, 30))

        # 设置operation_type
        operation_type = "Update"

        # 执行插入语句
        insert_query = f"INSERT INTO {table_name} (stock_id, start_date, end_date, operation_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (stock_id, start_date, end_date, operation_type))

def main():
    try:
        # 建立数据库连接
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aaqqRew???sett",
            database="Task"  # 确保这是正确的数据库名
        )
    except Error as e:
        print("Failed to connect to database:", e)
        return

    cursor = connection.cursor()

    # 要插入的股票ID列表
    stock_ids = ['sh600000', 'sh600011', 'sh600012', 'sh600023', 'sh600004', 'sh600015', 'sh600006', 'sh600007', 'sh600008', 'sh600009']

    # 插入数据到 User_tasks 表
    insert_data(cursor, "User_tasks", stock_ids)

    # 提交事务
    connection.commit()

    print("Data inserted successfully.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()

