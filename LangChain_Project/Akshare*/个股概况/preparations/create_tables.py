import mysql.connector


# connection
test_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aaqqRew???sett"
)


c = test_db.cursor()

c.execute("USE Stock")

c.execute(
  '''
  CREATE TABLE 个股概况 (
  Indexs varchar(10),
  Total_Market_Capitalization DECIMAL(20,6),
  Circulating_Market_Capitalization DECIMAL(20,6),
  Industry varchar(20),
  Listing_Date date,
  Stock_id varchar(10),
  Stock_name varchar(10),
  Total_Shares_Outstanding DECIMAL(20,1),
  Shares_in_Circulation DECIMAL(20,1)
  );
  ''')


c.close()
test_db.close()