from mysql.connector import Error
import mysql

def Initialize_databases(c):
	database_name = "Stock_sh"

	#check if database exists
	c.execute(f"SHOW DATABASES LIKE '{database_name}'")
	database_exists = c.fetchone() is not None

	if not database_exists:
		c.execute(f"CREATE DATABASE {database_name}")

	database_name = "Task"

	#check if database exists
	c.execute(f"SHOW DATABASES LIKE '{database_name}'")
	database_exists = c.fetchone() is not None

	if not database_exists:
		c.execute(f"CREATE DATABASE {database_name}")

	c.execute("SHOW DATABASES")

	for x in c:
		print(x)




def Initialize():
	#connect to local server
	try:
		# connection
		test_db = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  password="aaqqRew???sett"
		)
	except Error as e:
		print("Failed to connect to database")
		return

	c = test_db.cursor()

	Initialize_databases(c)
	Initialize_Tables(c)

	c.close()
	test_db.close()

	return

def Initialize_Tables(c):

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


    c.execute(f"SHOW TABLES LIKE 'CSI_INDEX_300'")
    table_exists = c.fetchone() is not None


    if not table_exists:
    	c.execute(
			'''
			CREATE TABLE CSI_INDEX_300 (
				date DATE PRIMARY KEY,
				open DECIMAL(10, 3),
				high DECIMAL(10, 3),
				low DECIMAL(10, 3),
				close DECIMAL(10, 3),
				volume BIGINT
				);
			''')

    c.execute("SHOW TABLES")
    print("Here are all tables in Stock_sh:")

    for x in c:
        print(x)

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

    return





