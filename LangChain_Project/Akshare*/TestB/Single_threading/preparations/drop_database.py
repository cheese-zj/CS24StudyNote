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

	# cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
    # database_exists = cursor.fetchone() is not None


	database_name = "Stock_single"

	c = test_db.cursor()

	#check if database exists
	c.execute(f"SHOW DATABASES LIKE '{database_name}'")
	database_exists = c.fetchone() is not None

	if database_exists:
		c.execute(f"DROP DATABASE {database_name}")


	c.execute("SHOW DATABASES")
	for x in c:
		print(x)

	c.close()
	test_db.close()

if __name__ == "__main__":
	main()