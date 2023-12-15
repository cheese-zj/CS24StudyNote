# SQL
`SQL keywords are NOT case sensitive: select is the same as SELECT`

## Installation&Setup
**Intallation**
```
https://www.youtube.com/watch?v=7S_tz1z_5bA
```

**Database**

Run the ``SQL Course Materials/create-databases.sql``:

Click the ``yellow thunder icon`` above
or
``Command+shift+Enter``(MacOs)

## Statements

### USE
Suppose that we have 2 databases ``database1`` and ``database2`` , 
if we want to work on ``database1``, we can simply use

```sql
USE database1;
```

switch to ``database2`` 

```sql
USE database2;
```

### SELECT
__Syntax__

```sql
SELECT column1, column2, ...
FROM table_name;
```

``*`` stands for all columns, statement below will return all columns in table

```sql
SELECT * FROM table_name;
```

The `SELECT DISTINCT` statement is used to return only distinct(different) values

```sql
SELECT DISTINCT column1, column2, ... FROM table_name
```

__Examples__:

3elects three columns from the customers table: ``first_name``, ``last_name``, and ``points``. The ``points`` column is multiplied by 1.2, and this calculated value is displayed as a column named ``scaled points``.

```sql
SELECT 
	first_name,
	last_name,
    points * 1.2 As 'scaled points'
FROM customers
```

Don't forget to use ``USE sql_store`` to choose the database

### WHERE
__Syntax__

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

__Examples:__

Retrieve the ``first_name`` and ``last_name`` from records where the ``first_name`` is ``'Babara'``.

```sql
SELECT first_name,last_name 
FROM customers
WHERE first_name='Babara'
```

Retrieve all customers' record where the ``birth_date`` is after ``'1980-01-01'``

```sql
SELECT * FROM customers
WHERE birth_date >= '1980-01-01'
```

### ORDER BY

__Syntax__

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

__Example__

Selects all columns from the ``order_items`` table, calculates the total price for each item by multiplying ``unit_price`` by ``quantity``, and orders the results first by ``order_id`` in ascending order, then by the calculated ``total price`` in descending order.

```sql
SELECT 
	*,
    unit_price * quantity AS 'Total Price'
FROM order_items
ORDER BY order_id ASC , unit_price * quantity DESC
```

### LOGIC OPERATION

__AND__: 
This operator is used to combine 2 conditions, and it returns true only if both conditions are true. For example, 
``SELECT * FROM table WHERE condition1 AND condition2;``
retrieves rows where both condition1 and condition2 are true.

__OR__: This operator is used to combine two conditions, and it returns true if either of the conditions is true. For example, 
``SELECT * FROM table WHERE condition1 OR condition2;`` 
retrieves rows where either condition1 or condition2 (or both) are true.

__NOT__: This operator is used to negate a condition, returning true if the condition is false. For example, 
``SELECT * FROM table WHERE NOT condition;`` 
retrieves rows where condition is not true.


### IN

__Syntax__

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

__Example__


```sql
SELECT *
FROM customers
WHERE state IN ('MA','VA','CO')
```


### Between

__Syntax__

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```
__\[value1,value2\]__

__Example__

__\['1980-01-01','1990-01-01'\]__
```sql
SELECT *
FROM customers
WHERE birth_date BETWEEN '1980-01-01' AND '1990-01-01'
```

### LIKE

__Syntax__


__The percent sign % represents zero, one, or multiple characters__
__The underscore sign _ represents one, single character__


```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

__Example__

```sql
SELECT *
FROM customers
WHERE city LIKE '%a' OR last_name LIKE 'M________y'
```

### NULL VALUES

A field with a __NULL value__ is a field with __no value__.

If a field in a table is optional, it is possible to insert a new record or update a record __without adding a value__ to this field. Then, the field will be saved with a __NULL value__.


__Test for NULL Values__

```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

```sql
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```


### LIMIT

__Syntax__

```sql
SELECT column_names
FROM table_name
LIMIT 10 
-- this is first 10 rows
```

```sql
SELECT column_names
FROM table_name
LIMIT 5,10 
-- skip first 5 rows, show 6 - 15
```

### __INNER JOIN__

__Syntax__

```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

__Example__

```sql
SELECT order_id,o.customer_id,first_name,last_name
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
```

### JOIN between different databases

__Syntax__

```sql

```

### INSERT INFO
The ``INSERT INTO`` statement is used to insert new __records__ in a table.




