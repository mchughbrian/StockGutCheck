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

# Initialize an empty list to store the tickers that meet the criteria
selected_tickers = []

for ticker in sp500_tickers:
        try:
            stock = yf.Ticker(ticker)

            # Fetch key statistics
            info = stock.info
            pe_ratio = info['trailingPE']
            pb_ratio = info['priceToBook']
            dividend_yield = info['dividendYield']

            if (pe_ratio < pe_ratio_threshold and
                pb_ratio < pb_ratio_threshold and
                dividend_yield > dividend_yield_threshold):

                # Add the ticker to the selected_tickers list
                selected_tickers.append(ticker)

        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

print(selected_tickers)