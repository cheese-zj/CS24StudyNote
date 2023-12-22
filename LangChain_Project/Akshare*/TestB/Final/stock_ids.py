import akshare as ak
import pandas as pd

# 获取所有A股的实时数据
stock_zh_a_spot_df = ak.stock_zh_a_spot()

# 提取股票代码列
stock_codes = stock_zh_a_spot_df['代码']

# 筛选出以 'sh' 开头的股票代码（沪市股票）
sh_stock_codes = stock_codes[stock_codes.str.startswith('sh')]

# 按照股票代码最后一位数字进行分组，并从每组中选择一个代表
selected_stocks = []
for i in range(10):
    # 筛选出以特定数字结尾的股票代码
    stocks_with_specific_end = sh_stock_codes[sh_stock_codes.str.endswith(str(i))]

    # 如果该类股票存在，从中选择一个
    if not stocks_with_specific_end.empty:
        selected_stock = stocks_with_specific_end.iloc[0]
        selected_stocks.append(selected_stock)

# 打印所选股票代码
print(selected_stocks)
