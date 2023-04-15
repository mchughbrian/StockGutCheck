#This code is to apply Ben Grahms Value investing Principles

import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup

# Fetch S&P 500 components
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
rows = table.find_all('tr')[1:]
sp500_tickers = [row.find_all('td')[0].text.strip() for row in rows]

# Define screening criteria
pe_ratio_threshold = 15
pb_ratio_threshold = 1.5
dividend_yield_threshold = 0.02
debt_to_equity_threshold = 0.5
earnings_growth_threshold = 0.05
financial_modeling_prep_api_key = 'your_api_key_here'

# Initialize a DataFrame to store the results
screened_stocks = pd.DataFrame(columns=['Ticker', 'P/E Ratio', 'P/B Ratio', 'Dividend Yield', 'Debt to Equity', '5-Year Earnings Growth'])


