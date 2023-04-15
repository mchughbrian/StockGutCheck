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

