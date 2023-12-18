import mysql.connector


# this is local connection
# need to wrap by try-cathch block
test_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aaqqRew???sett"
)

c = test_db.cursor()



c.excecute("SELECT * FROM ")



c.close()
test_db.close()
