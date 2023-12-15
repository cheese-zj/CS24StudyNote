# Python MYSQL



## Installation
##### MYSQLWorkbench
please see `LangChain_Project/SQL Course Materials/Guide.md`

##### MySQL Driver
MACOS 

Run this command on Terminal(Make sure you have pip)
```shell
pip install mysql-connector-python
```

to test if you intall successfully,
```shell
python3
```

then

```shell
import mysql.connector
```

if there is no message, all good.


## Usage

### Create Database

```python
import mysql.connector

test_db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

c = test_db.cursor()

c.execute("CREATE DATABASE DATABASE_NAME")
```

__to check if database exists__

```python
c.execute("SHOW DATABASES")

for x in c:
  print(x)
```

__`information_schema`,`mysql`,`performance_schema`,`sys` are default databases.__


### Drop Database
```python
c = test_db.cursor()
c.execute("DROP DATABASE DATABASE_NAME")
```

### Create Table
```python
c = test_db.cursor()

# select the database
c.execute("USE DATABASES_NAME")

# create table

c.execute(
	'''
	CREATE TABLE customers 
	(
		# column_name data_type
		name VARCHAR(255), 
		address VARCHAR(255)
	)
	'''
	)
```

__to check if table exists__

```python
c.execute("SHOW TABLES")

for x in c:
  print(x)
```

### Insert Values

```python
import mysql.connector

#... make the connection

c = test_db.cursor()

c.execute("USE stock_analysis")

sql = "INSERT INTO stock VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
values = [
  ('600570','恒生电子','2023-12-01','30.02','30.76','30.92','29.94','186800'),

  # Be carefull, DEFAULT in Mysql is None in python
  ('600570','恒生电子','2023-12-02',None,None,None,None,None),
  #...
  #...
  ('600570','恒生电子','2023-12-12','30.17','29.72','30.24','29.56','223200'),
  ('600570','恒生电子','2023-12-13','29.78','29.34','30.16','29.33','235900')
]


c.executemany(sql, values)

# do not forget this line!!!!
test_db.commit()

print(c.rowcount)

c.close()
test_db.close()
```
