# TestB

## Overview
一个针对AKshare接口的自动取数，并进行若干投研场景实现的简单分析。 

## Purpose
实现针对上证A股指数(沪深300的日线、周线、月线)，A股公司的日K线数据获取计算，并输出指数的周线连跌天数下周期，及个股情况


## Data Initialization
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
##### 当前
__Database__: `Task`  Store tasks need to be finished 

__Tables__:
- User_tasks 
User's input, these tasks should be executed based on user's will
```sql
CREATE TABLE {table_name} (
    stock_id VARCHAR(10),
    start_date DATE,
    end_date DATE,
    operation_type VARCHAR(10),
    PRIMARY KEY (stock_id, start_date, end_date)
);
```

- Daily_tasks
Daily tasks,should be executed at a certain time point
```sql
CREATE TABLE {table_name} (
    stock_id VARCHAR(10),
    start_date DATE,
    end_date DATE,
    operation_type VARCHAR(10),
    PRIMARY KEY (stock_id, start_date, end_date)
);
```

__Database__: `Stock_sh`  存储沪A股的日k线数据:

__Tables__:
A_share[0-9]

```sql
CREATE TABLE {table_name} (
    stock_id VARCHAR(10),
    date DATE,
    open DECIMAL(10, 3),
    high DECIMAL(10, 3),
    low DECIMAL(10, 3),
    close DECIMAL(10, 3),
    amount BIGINT,
    PRIMARY KEY (stock_id ,date)
);
```

__优化方向__:
- 索引要加吗
- 临时表池
- 连接池

### 设计Python代码，实现数据获取及数据库数据写入(单线程)
Updated soon
Now in `Single_threading`

### 优化代码，实现多线程的并发查询和写入(2线程)

__优化方向__:
- 错误处理
- 日志和监控
- 批量插入 
- 修复 dir 中的锁等待问题
- 用户交互

## Application

### 计算生成A股指数的周线、月线，连阴天数及对应的时间周期(如，7周（3月），20210101-20210220) 
### 计算生成个股的相关信息 
### 提供函数方法，针对证券编号、过滤类型(周线、月线)，持续时间(int)返回最终结果数据。
