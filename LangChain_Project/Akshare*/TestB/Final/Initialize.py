from mysql.connector import Error
import mysql.connector

def check_and_create_database(cursor, database_name):
    cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
    if cursor.fetchone() is None:
        cursor.execute(f"CREATE DATABASE {database_name}")

def check_and_create_table(cursor, database_name, table_name, create_table_sql):
    cursor.execute(f"USE {database_name}")
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    if cursor.fetchone() is None:
        cursor.execute(create_table_sql)

def initialize_databases(cursor):
    databases = ["Stock_sh", "Task"]
    for db in databases:
        check_and_create_database(cursor, db)

def initialize_tables(cursor):
    # Stock_sh database tables
    cursor.execute("USE Stock_sh")
    for i in range(10):
        table_name = f"A_share{i}"
        create_table_sql = f'''CREATE TABLE {table_name} (
                                stock_id VARCHAR(10),
                                date DATE,
                                open DECIMAL(10, 3),
                                high DECIMAL(10, 3),
                                low DECIMAL(10, 3),
                                close DECIMAL(10, 3),
                                amount BIGINT,
                                PRIMARY KEY (stock_id, date)
                              );'''
        check_and_create_table(cursor, "Stock_sh", table_name, create_table_sql)

    # Additional Stock_sh tables
    csi_index_table_sql = '''
                            CREATE TABLE CSI_INDEX_300 (
                                date DATE PRIMARY KEY,
                                open DECIMAL(10, 3),
                                high DECIMAL(10, 3),
                                low DECIMAL(10, 3),
                                close DECIMAL(10, 3),
                                volume BIGINT
                            );
                          '''
    stock_ids_table_sql = '''
                          CREATE TABLE stock_ids (
                              id VARCHAR(20) PRIMARY KEY
                          );
                          '''
    check_and_create_table(cursor, "Stock_sh", "CSI_INDEX_300", csi_index_table_sql)
    check_and_create_table(cursor, "Stock_sh", "stock_ids", stock_ids_table_sql)

    # Task database tables
    cursor.execute("USE Task")
    user_tasks_table_sql = '''
                           CREATE TABLE User_tasks (
                               stock_id VARCHAR(10),
                               start_date DATE,
                               end_date DATE,
                               operation_type VARCHAR(10),
                               PRIMARY KEY (stock_id, start_date, end_date)
                           );
                           '''
    daily_tasks_table_sql = '''
                            CREATE TABLE Daily_tasks (
                                stock_id VARCHAR(10),
                                start_date DATE,
                                end_date DATE,
                                operation_type VARCHAR(10),
                                PRIMARY KEY (stock_id, start_date, end_date)
                            );
                            '''
    check_and_create_table(cursor, "Task", "User_tasks", user_tasks_table_sql)
    check_and_create_table(cursor, "Task", "Daily_tasks", daily_tasks_table_sql)

def initialize():
    try:
        test_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aaqqRew???sett"
        )
    except Error as e:
        print("Failed to connect to database:", e)
        return

    cursor = test_db.cursor()

    initialize_databases(cursor)
    initialize_tables(cursor)

    cursor.close()
    test_db.close()



