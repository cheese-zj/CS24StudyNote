# TestB

## Overview
一个针对AKshare接口的自动取数，并进行若干投研场景实现的简单分析。 

## Purpose
实现针对上证A股指数(沪深300的日线、周线、月线)，A股公司的日K线数据获取计算，并输出指数的周线连跌天数下周期，及个股情况


## Data Initialization
__time limitation: 12 months__
### 针对要求，寻找AKshare接口信息
- 沪深300
```
https://akshare.akfamily.xyz/tutorial.html#id1
```
- A股公司
```
https://akshare.akfamily.xyz/data/stock/stock.html#id13
```

### 针对接口信息创建数据库表结构
__python script => bash 集成__
`check.py` __check if databases,tables exsits, if not, automatically create__

`create_database.py` __create `Stock` database__
`create_tables.py` __create `沪深300`,`A股`表格__
`drop_database.py` __delete `Stock` database if exists__

### 设计Python代码，实现数据获取及数据库数据写入(单线程)

due:2023.12.20 24:00

### 优化代码，实现多线程的并发查询和写入(2线程)

## Application

### 计算生成A股指数的周线、月线，连阴天数及对应的时间周期(如，7周（3月），20210101-20210220) 
### 计算生成个股的相关信息 
### 提供函数方法，针对证券编号、过滤类型(周线、月线)，持续时间(int)返回最终结果数据。 