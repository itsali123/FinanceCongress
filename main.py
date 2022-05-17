#!/usr/bin/env python
import pandas as pd
import pandas_datareader.data as web
from pandas import Series, DataFrame
import datetime
from datetime import date, timedelta
import matplotlib as mpl
from matplotlib import pyplot as plt
# Get stock from user
# stock = input("Please enter your stock: ")

# Iterate through stock list
ticker_list = ["MSFT", "AAPL", "AMZN"]
x = len(ticker_list)
x = x-1


for ticker in ticker_list:
    # Specify date range
    start = datetime.datetime(2020, 2, 2)
    end = datetime.datetime(2021, 2, 2)

    # Grab stock info from yahoo, start to end
    df = web.DataReader(ticker_list[x], 'yahoo', start, end)

    # Find 30 day moving average for price
    df['Price_Moving_Avg'] = df['Adj Close'].rolling(window=30).mean()
    # Find moving average volume for the last 30 days
    df['Vol_Moving_Avg'] = df['Volume'].rolling(window=30).mean()

    # print(ticker_list[x], df)
    df = df[df['Price_Moving_Avg'].notna()]
    # print(ticker_list[x], df)
    # plt the moving average
    close_price = df["Adj Close"]
    mavgplot = df["Price_Moving_Avg"]
    vmagplot = df["Vol_Moving_Avg"]

    # Adjusting the size of matplotlib
    mpl.rc('figure', figsize=(15, 10))

    # Adjusting the size of matplotlib
    # mpl.style.use('ggplot')

    close_price.plot(label=ticker_list[x], legend=True)
    mavgplot.plot(label='mavg=30d', legend=True)
    vmagplot.plot(secondary_y=True, label='Volume Avg 30d', legend=True)
    plt.savefig(str(ticker_list[x]) + '.png')

    x = x-1
