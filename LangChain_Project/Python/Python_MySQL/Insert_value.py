import mysql.connector


# connection
test_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aaqqRew???sett"
)

c = test_db.cursor()

c.execute("USE stock_analysis")

sql = "INSERT INTO stock VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
values = [
  ('600570','恒生电子','2023-12-01','30.02','30.76','30.92','29.94','186800'),
  ('600570','恒生电子','2023-12-02',None,None,None,None,None),
  ('600570','恒生电子','2023-12-03',None,None,None,None,None),
  ('600570','恒生电子','2023-12-04','30.61','30.58','30.86','30.41','170700'),
  ('600570','恒生电子','2023-12-05','30.49','29.39','30.50','29.39','238800'),
  ('600570','恒生电子','2023-12-06','29.40','29.14','29.50','28.73','256400'),
  ('600570','恒生电子','2023-12-07','29.10','29.14','29.37','28.70','200700'),
  ('600570','恒生电子','2023-12-08','29.07','29.46','29.74','29.04','223200'),
  ('600570','恒生电子','2023-12-09',None,None,None,None,None),
  ('600570','恒生电子','2023-12-10',None,None,None,None,None),
  ('600570','恒生电子','2023-12-11','29.38','30.21','30.39','28.88','273600'),
  ('600570','恒生电子','2023-12-12','30.17','29.72','30.24','29.56','223200'),
  ('600570','恒生电子','2023-12-13','29.78','29.34','30.16','29.33','235900')
]

c.executemany(sql, values)

test_db.commit()

print(c.rowcount)

c.close()
test_db.close()