#!/usr/bin/env python
import pandas as pd
import pandas_datareader.data as web
from pandas import Series, DataFrame
import datetime
from datetime import date

# Get stock from user
stock = input("Please enter your stock: ")

# Specify date range
start = datetime.datetime(2020, 2, 2)
end = datetime.datetime(2021, 2, 2)

# Grab stock info from yahoo, start to end
df = web.DataReader(stock, 'yahoo', start, end)
print(df)