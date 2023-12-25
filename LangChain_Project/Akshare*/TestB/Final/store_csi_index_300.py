import mysql.connector
from mysql.connector import Error
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import akshare as ak

def write_to_db(engine):
    try:
        with engine.begin() as conn:
            # 创建临时表
            tmp_table_name = "CSI_INDEX_300_temp"

            # 获取沪深300指数的日线数据
            stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sh000300")
            stock_zh_index_daily_df['date'] = pd.to_datetime(stock_zh_index_daily_df['date']).dt.date
            stock_zh_index_daily_df.to_sql(name=tmp_table_name, con=engine, if_exists='replace', index=False)

            # 使用SQL查询从临时表中筛选出2023年及以后的数据，并插入或更新到主表
            insert_query = text(f"""
            INSERT INTO CSI_INDEX_300 (date, open, high, low, close, volume)
            SELECT date, open, high, low, close, volume
            FROM {tmp_table_name}
            ON DUPLICATE KEY UPDATE
                open = VALUES(open),
                high = VALUES(high),
                low = VALUES(low),
                close = VALUES(close),
                volume = VALUES(volume)
            """)
            result = conn.execute(insert_query)
        print("Data written to database successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the database: {e}")

def run():
    try:
        # 数据库配置
        database_url = "mysql+pymysql://root:aaqqRew???sett@localhost:3306/Stock_sh"
        engine = create_engine(database_url)

        # 将数据写入数据库
        write_to_db(engine)
    except Error as db_error:
        print(f"Database error: {db_error}")
    except Exception as e:
        print(f"An error occurred: {e}")

