import mysql.connector

test_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aaqqRew???sett"
)


# Oh dude, this is a fuckin object
# alright, everything is object in python
print(test_db)

test_db.close()