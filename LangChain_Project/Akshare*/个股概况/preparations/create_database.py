import mysql.connector


# this is local connection
test_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aaqqRew???sett"
)


c = test_db.cursor()


c.execute("CREATE DATABASE Stock")


c.close()
test_db.close()
