# import akshare as ak
# import mysql.connector
# import pandas as pd
# from sqlalchemy import create_engine, text, MetaData, Table
# import json
# from datetime import datetime, timedelta, date
# from concurrent.futures import ThreadPoolExecutor
# import sup
# import traceback
# import time
# import logging
# import os

import write_data as W
import Initialize as I
import CSI_INDEX_300_STORE as C

def main():
    I.Initialize()
    while True:
        print()
        print("Here are your options:")
        print("1.Update CSI_INDEX_300")
        print("2.Finish all tasks")
        print("3.search value")
        print("6.exit")

        a = input("")
        if a == "1":
            C.run()
        elif a == "2":
            W.wr_data()
        elif a == "6":
            break

    return

if __name__=="__main__":
    main()

