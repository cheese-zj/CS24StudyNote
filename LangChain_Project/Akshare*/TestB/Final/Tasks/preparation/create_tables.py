from mysql.connector import Error
import mysql.connector

def main():
    # 连接到本地服务器
    try:
        # 建立连接
        test_db = mysql.connector.connect(
          host="localhost",
          user="root",
          password="aaqqRew???sett"
        )
    except Error as e:
        print("Failed to connect to database:", e)
        return

    c = test_db.cursor()
    c.execute("USE Task")

    table_name = "User_tasks"

    c.execute(f"SHOW TABLES LIKE '{table_name}'")
    table_exists = c.fetchone() is not None

    # 如果表不存在，则创建
    if not table_exists:
        c.execute(
            f'''
            CREATE TABLE {table_name} (
                stock_id VARCHAR(10),
                start_date DATE,
                end_date DATE,
                operation_type VARCHAR(10),
                PRIMARY KEY (stock_id, start_date, end_date)
            );
                ''')


    table_name = "Daily_tasks"

    c.execute(f"SHOW TABLES LIKE '{table_name}'")
    table_exists = c.fetchone() is not None
    # 如果表不存在，则创建
    if not table_exists:
        c.execute(
            f'''
            CREATE TABLE {table_name} (
                stock_id VARCHAR(10),
                start_date DATE,
                end_date DATE,
                operation_type VARCHAR(10),
                PRIMARY KEY (stock_id, start_date, end_date)

            );
                ''')


    c.execute("SHOW TABLES")
    print("Here are all tables in Task:")

    for x in c:
        print(x)

    c.close()
    test_db.close()

if __name__ == "__main__":
    main()