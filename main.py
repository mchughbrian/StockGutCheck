#This code is to apply Ben Grahms Value investing Principles

import pandas as pd
import yfinance as yf
import requests

# Fetch S&P 500 components
sp500_table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
sp500_tickers = sp500_table['Symbol'].tolist()
