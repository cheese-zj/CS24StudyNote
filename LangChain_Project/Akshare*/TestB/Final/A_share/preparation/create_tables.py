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
    c.execute("USE Stock_sh")

    # 创建10个表
    for i in range(10):
        table_name = f"A_share{i}"

        c.execute(f"SHOW TABLES LIKE '{table_name}'")
        table_exists = c.fetchone() is not None

        # 如果表不存在，则创建
        if not table_exists:
            c.execute(
                f'''
                CREATE TABLE {table_name} (
                    stock_id VARCHAR(10),
                    date DATE,
                    open DECIMAL(10, 3),
                    high DECIMAL(10, 3),
                    low DECIMAL(10, 3),
                    close DECIMAL(10, 3),
                    amount BIGINT,
                    PRIMARY KEY (stock_id ,date)
                );
                ''')

    c.execute("SHOW TABLES")
    print("Here are all tables in Stock_sh:")

    for x in c:
        print(x)

    c.close()
    test_db.close()

if __name__ == "__main__":
    main()
