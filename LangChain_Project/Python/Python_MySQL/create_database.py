import mysql.connector


# connection
test_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aaqqRew???sett"
)


c = test_db.cursor()


c.execute("CREATE DATABASE stock_analysis")

# check if database exsits
c.execute("SHOW DATABASES")

for x in c:
  print(x)


c.close()
test_db.close()

