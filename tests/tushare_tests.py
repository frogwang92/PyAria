import tushare as ts
import pandas as pd


df = ts.get_tick_data('600000', date='2016-11-18')
df.to_csv('test.csv')
print(df.head())
