import akshare as ak
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, text, MetaData, Table
import json
from datetime import datetime, timedelta, date
from concurrent.futures import ThreadPoolExecutor
import sup
import traceback
import time
import logging
import os
import matplotlib.pyplot as plt
import mplfinance as mpf


def weekly_line(start_date, end_date):
    engine = sup.create_db_engine('Config/Stock_sh_db.json')

    query = f"SELECT * FROM CSI_INDEX_300 WHERE date BETWEEN '{start_date}' AND '{end_date}'"  # 注意这里添加了结束日期的单引号

    df = pd.read_sql(query, engine)


    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # 计算周线和月线
    df_weekly = df.resample('W').agg({'open': 'first', 
                                      'high': 'max', 
                                      'low': 'min', 
                                      'close': 'last', 
                                      'volume': 'sum'})
    df_monthly = df.resample('M').agg({'open': 'first', 
                                       'high': 'max', 
                                       'low': 'min', 
                                       'close': 'last', 
                                       'volume': 'sum'})
    save_params = dict(
	    fname='graphs/weekly_line_chart.png',  # 文件名和路径
	    dpi=100,                        # 图像分辨率
	    pad_inches=0.25                 # 周围边缘空间
	)
    mpf.plot(df_weekly, type='candle', title='CSI INDEX 300 Weekly Line', ylabel='Index Value', savefig=save_params)
    save_params['fname'] = 'graphs/monthly_line_chart.png'
    mpf.plot(df_monthly, type='candle', title='CSI INDEX 300 Monthly Line', ylabel='Index Value', savefig=save_params)





weekly_line('2019-01-01', '2023-12-20')
