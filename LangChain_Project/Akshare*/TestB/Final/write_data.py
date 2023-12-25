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

def setup_logging():
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_filename = f"{current_datetime}.log"
    logging.basicConfig(filename=os.path.join(log_directory, log_filename),
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s:%(message)s')

def Update_to_db_direct(engine, engine_Task, item, max_retries=3):
    for attempt in range(max_retries):
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

                logging.info(f"Deleted data from {main_table_name} for stock ID {item[0]} between {start_date_formatted} and {end_date_formatted}")

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
                    logging.info(f"Data insertion verified successfully, updated {result[0]} records in table {main_table_name}.")
                    
                    with engine_Task.begin() as conn_task:
                        delete_task_query = text("""
                        DELETE FROM User_tasks
                        WHERE stock_id = :stock_id AND start_date = :start_date AND end_date = :end_date
                        """)
                        conn_task.execute(delete_task_query, {'stock_id': item[0], 'start_date': item[1], 'end_date': item[2]})
                        logging.info(f"Deleted completed task for stock ID {item[0]} from User_tasks.")

                else:
                    logging.warning(f"Data insertion verification failed, expected {len(stock_data)} records, but updated {result[0]}.")

            break

        except Exception as e:
            logging.error(f"Error updating database: {e}")
            traceback.print_exc()

            if attempt == max_retries - 1:
                logging.critical("Reached maximum retry limit, operation failed")
                raise

def process_group(db_config_file, engine_Task, group):
    local_engine = sup.create_db_engine(db_config_file)
    for item in group:
        try:
            Update_to_db_direct(local_engine, engine_Task, item)
        except Exception as e:
            logging.error(f"Error processing group {group} with item {item}: {e}")

def wr_data():
    setup_logging()  # 设置日志
    db_config_stock_sh = 'Config/Stock_sh_db.json'
    engine_Task = sup.create_db_engine('Config/Task_db.json')

    items = sup.read_Tasks(engine_Task, "User_tasks")

    grouped_items = sup.group_items_by_hash_id(items)

    with ThreadPoolExecutor(max_workers=5) as executor:
        for group in grouped_items:
            executor.submit(process_group, db_config_stock_sh, engine_Task, group)

    logging.info("All tasks processed successfully.")


