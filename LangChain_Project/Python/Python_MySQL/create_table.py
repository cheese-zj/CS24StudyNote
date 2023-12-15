import mysql.connector


# connection
test_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aaqqRew???sett"
)


c = test_db.cursor()

c.execute("USE stock_analysis")

c.execute(
  '''
  CREATE TABLE stock (
  stock_id varchar(16) NOT NULL,
  stock_name varchar(64) NOT NULL,
  date DATE NOT NULL,
  open_price DECIMAL(10,2) DEFAULT NULL,
  close_price DECIMAL(10,2) DEFAULT NULL,
  high_price DECIMAL(10,2) DEFAULT NULL,
  low_price DECIMAL(10,2) DEFAULT NULL,
  volume DECIMAL(10,2) DEFAULT NULL,
  PRIMARY KEY (stock_id, date)
  );
  ''')

c.execute("SHOW TABLES")

for x in c:
  print(x)

c.close()
test_db.close()