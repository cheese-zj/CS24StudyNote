import akshare as ak
import pandas as pd
import mysql.connector
from tqdm import tqdm  # 引入 tqdm
from datetime import datetime



def is_valid_date(string):
    # 首先检查字符串是否为8位数字
    if len(string) == 8 and string.isdigit():
        try:
            # 尝试将其按照 YYYYMMDD 格式解析为日期
            datetime.strptime(string, '%Y%m%d')
            return True
        except ValueError:
            return False
    return False

def is_number(s):
    try:
        float(s)  # 尝试转换为浮点数
        return True
    except ValueError:
        return False

def check_type(data:str,index:int):

  # check if it is a number
  if index in [0,1,6,7]:

    if is_number(data):
      #is number, keep the value
      return data

    else:
      #not a number, return None
      return None

  if index==3:
    if is_valid_date(str(data)):
      return data
    else: 
      return None

  return data

def main():
  # connection
  test_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aaqqRew???sett"
  )

  c = test_db.cursor()
  c.execute("USE Stock")

  sql = "INSERT INTO 个股概况 VALUES (%s, %s, %s, %s, %s, %s, %s, %s ,%s)"

  # 获取股票列表
  stock_list = ak.stock_zh_a_spot_em()
  stock_codes = stock_list['代码']

  index = 0

  for code in tqdm(stock_codes):  # 使用 tqdm 包裹循环

    # 获取每只股票的信息
    stock_data = ak.stock_individual_info_em(symbol=code)
    value = []


    value.append(index)
    # 把stock_data中的value列的值存成 tuple value
    for i in range(len(stock_data["value"])):
      value.append(check_type(stock_data["value"][i],i))

    value = tuple(value)
    c.execute(sql,value)
    index += 1

  test_db.commit()
  c.close()
  test_db.close()

  return

def test():
    # connection
  test_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aaqqRew???sett"
  )

  c = test_db.cursor()
  c.execute("USE Stock")

  sql = "INSERT INTO 个股概况 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

  # 获取股票列表
  stock_list = ak.stock_zh_a_spot_em()
  stock_codes = stock_list['代码']
  code = stock_codes[866]


  stock_data = ak.stock_individual_info_em(symbol=code)
  print(stock_data)
  value = []

  # 把stock_data中的value列的值存成 tuple value
  for i in range(len(stock_data["value"])):
    value.append(check_type(stock_data["value"][i],i))

  value = tuple(value)
  c.execute(sql,value)


  test_db.commit()
  c.close()
  test_db.close()

  return


if __name__ == "__main__":
  main()
  #test()

