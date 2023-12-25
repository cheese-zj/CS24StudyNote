import akshare as ak
import pandas as pd
import json
import sup
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

def get_a_stock_data():
    """获取所有A股的实时数据"""
    try:
        return ak.stock_zh_a_spot()
    except Exception as e:
        print(f"Error in getting A-share data: {e}")
        return None

def filter_sh_stock_codes(stock_data):
    """筛选出以 'sh' 开头的股票代码（沪市股票）"""
    try:
        stock_codes = stock_data['代码']
        return stock_codes[stock_codes.str.startswith('sh')]
    except Exception as e:
        print(f"Error in filtering SH stock codes: {e}")
        return pd.Series()

def store_stock_ids(engine, stock_codes):
    try:
        with engine.begin() as conn:
            tmp_table_name = "stock_ids_tmp"
            main_table_name = "stock_ids"
            # 将 Series 转换为 DataFrame
            stock_codes = stock_codes.to_frame(name='id')

            # 将数据转换为 DataFrame 并写入临时表
            stock_codes.to_sql(name=tmp_table_name, con=conn, if_exists='replace', index=False)

            # 插入或更新数据到主表
            insert_query = text(f"""
            INSERT INTO {main_table_name} (id)
            SELECT id FROM `{tmp_table_name}`
            ON DUPLICATE KEY UPDATE id = VALUES(id);
            """)

            conn.execute(insert_query)

            # 删除临时表
            drop_query = text(f"DROP TABLE IF EXISTS `{tmp_table_name}`")
            conn.execute(drop_query)

    except Exception as e:
        print(f"An error occurred while writing to the database: {e}")

def updates():
    stock_data = get_a_stock_data()
    if stock_data is not None:
        sh_stock_codes = filter_sh_stock_codes(stock_data)
        engine = sup.create_db_engine('Config/Stock_sh_db.json')
        store_stock_ids(engine, sh_stock_codes)
    return


