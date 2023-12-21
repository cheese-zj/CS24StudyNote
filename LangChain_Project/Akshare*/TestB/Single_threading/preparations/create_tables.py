from mysql.connector import Error
import mysql

def main():
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

	database_name = "Stock_single"

	c = test_db.cursor()
	c.execute("USE Stock_single")

	c.execute(f"SHOW TABLES LIKE 'CSI_INDEX_300'")
	table_exists = c.fetchone() is not None

	# if table does not exist, then create
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
	print("Here are all tables in Stock_single")

	for x in c:
		print(x)

	c.close()
	test_db.close()

if __name__ == "__main__":
	main()