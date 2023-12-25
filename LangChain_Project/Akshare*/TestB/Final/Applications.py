import pandas as pd
from sqlalchemy import create_engine
import mplfinance as mpf
import json
import sup


def print_menu():
  print("Here are all the available functions:")
  print("1. Get a weekly graph")
  print("2. Get a monthly graph")
  print("3. Get max decline days")
  print("4. Get weekly data")
  print("5. Get monthly data")
  print("6. Individual stock overview")
  print("7. Exit")
  return

def individual_stock_overview(engine, stock_id, start_date, end_date, stock_type):
    try:
        # 根据股票类型选择表名和列名
        if stock_type == 'A':
            query = f"SELECT * FROM A_share{sup.hash_id_to_digit(stock_id)} WHERE stock_id = '{stock_id}' AND date BETWEEN '{start_date}' AND '{end_date}' ORDER BY date"
            volume_column = 'amount'
        elif stock_type == 'C':
            query = f"SELECT * FROM CSI_INDEX_300 WHERE date BETWEEN '{start_date}' AND '{end_date}' ORDER BY date"
            volume_column = 'volume'
        else:
            print("Invalid stock type.")
            return

        df = pd.read_sql(query, engine)

        if df.empty:
            print("No data available for the given stock ID and date range.")
            return

        # 计算基本统计数据
        latest_data = df.iloc[-1]
        high = df['high'].max()
        low = df['low'].min()
        average_volume = df[volume_column].mean()
        price_change = ((latest_data['close'] - df.iloc[0]['open']) / df.iloc[0]['open']) * 100

        # 输出个股概述
        print(f"Individual Stock Overview for {stock_id}")
        print(f"Latest Open: {latest_data['open']}, Close: {latest_data['close']}, High: {latest_data['high']}, Low: {latest_data['low']}")
        print(f"High (period): {high}, Low (period): {low}")
        print(f"Average Volume: {average_volume}")
        print(f"Price Change (%): {price_change:.2f}%")

    except Exception as e:
        print("Error in querying stock overview data:", e)

def calculate_consecutive_decline_days(df):
    # 初始化变量
    max_decline_days = 0
    current_decline_days = 0
    max_period = None
    current_start_date = None

    # 遍历DataFrame
    for date, row in df.iterrows():
        if row['close'] < row['open']:  # 下跌天（阴线）
            current_decline_days += 1
            if current_start_date is None:
                current_start_date = date
        else:  # 如果不是下跌天，则重置计数
            if current_decline_days > max_decline_days:
                max_decline_days = current_decline_days
                max_period = (current_start_date, date)
            current_decline_days = 0
            current_start_date = None

    # 检查最后一段下跌期
    if current_decline_days > max_decline_days:
        max_decline_days = current_decline_days
        max_period = (current_start_date, date)

    return max_decline_days, max_period


# 查询股票数据
def query_stock_data(engine, table_name, start_date, end_date):
    query = f"SELECT * FROM {table_name} WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    try:
        df = pd.read_sql(query, engine)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        return df
    except Exception as e:
        print("Error querying stock data:", e)
        return None

# 数据聚合函数
def aggregate_data(df, resample_period, stock_type):
    volume_column = 'amount' if stock_type == 'A Share' else 'volume'
    return df.resample(resample_period).agg({'open': 'first', 
                                             'high': 'max', 
                                             'low': 'min', 
                                             'close': 'last', 
                                             volume_column: 'sum'})

# 生成图表
def generate_graph(df_aggregated, title, file_name):
    save_params = {
        'fname': f'graphs/{file_name}',
        'dpi': 100,
        'pad_inches': 0.25
    }
    mpf.plot(df_aggregated, type='candle', title=title, ylabel='Index Value', savefig=save_params)

# 处理股票数据
def process_stock_data(start_date, end_date, stock_id, mode):
    engine = sup.create_db_engine('Config/Stock_sh_db.json')
    if engine is None:
        return

    # 根据股票ID判断股票类型
    stock_type = "A Share" if stock_id not in ["沪深300", "CSI 300", "沪深300指数"] else "CSI INDEX 300"
    table_name = f"A_share{sup.hash_id_to_digit(stock_id)}" if stock_type == "A Share" else "CSI_INDEX_300"

    df = query_stock_data(engine, table_name, start_date, end_date)
    if df is not None:
        resample_period = 'W' if mode.upper() == "WEEK" else 'M'
        df_aggregated = aggregate_data(df, resample_period, stock_type)
        file_name = f'{stock_id.lower()}_{mode.lower()}_line_chart.png'
        generate_graph(df_aggregated, stock_type, file_name)
        print(f"Graph generated: {file_name}")

# 示例调用
# process_stock_data('2023-01-01', '2023-12-31', 'CSI 300', 'WEEK')

def Menu():
    engine = sup.create_db_engine('Config/Stock_sh_db.json')
    if engine is None:
        print("Error: Unable to connect to the database.")
        return

    while True:
        print_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "7":
            print("Exiting the program.")
            break

        stock_type = input("Enter stock type (A for A Share, C for CSI 300): ").upper()

        if stock_type not in ['A', 'C']:
            print("Invalid stock type. Please enter 'A' or 'C'.")
            continue

        stock_id = input("Enter stock ID (e.g., sh600000): ")
        
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")

        start_date = sup.validate_date(start_date_str)
        end_date = sup.validate_date(end_date_str)

        if not start_date or not end_date:
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
            continue

        if end_date < start_date:
            print("End date must be after or equal to start date.")
            continue

        # Graphs
        if choice in ["1", "2"]:
            mode = "WEEK" if choice == "1" else "MONTH"
            if stock_type == 'C':
                stock_id = "CSI 300"  # 或者任何CSI 300指数的标识
            process_stock_data(start_date, end_date, stock_id, mode)


        # Data

        elif choice in ["4", "5"]:
            mode = "WEEK" if choice == "4" else "MONTH"
            if stock_type == 'C':
                stock_id = "CSI 300"  # 或者任何CSI 300指数的标识

            table_name = f"A_share{sup.hash_id_to_digit(stock_id)}" if stock_type == "A" else "CSI_INDEX_300"
            print(query_stock_data(engine, table_name, start_date, end_date))

        # 连阴天数
        elif choice == "3":

            if stock_type == 'C':
                stock_id = "CSI 300"  # 或者任何CSI 300指数的标识

            table_name = f"A_share{sup.hash_id_to_digit(stock_id)}" if stock_type == 'A' else "CSI_INDEX_300"
            df = query_stock_data(engine, table_name, start_date, end_date)

            if df is not None:
                max_decline_days, max_period = calculate_consecutive_decline_days(df)
                print(f"Max consecutive decline days: {max_decline_days}, Period: {max_period}")

            else:
                print("No data available for the given stock ID and date range.")

        #个股概述
        elif choice == "6":
            if stock_type == 'C':
                stock_id = "CSI 300"  # 或者任何CSI 300指数的标识

            individual_stock_overview(engine, stock_id, start_date, end_date ,stock_type)


        else:
            print("Invalid choice. Please enter a number between 1 and 6.")




