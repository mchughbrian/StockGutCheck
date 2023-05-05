# StockGutCheck
Please view code the visualization and competitive comparison part of the code in nbviewer (https://nbviewer.jupyter.org/github/mchughbrian/StockGutCheck/blob/main/Stock%20Exploration%20-%20Data%20Viz%20and%20structures.ipynb)
**Used Plotly to create interactive plots**

Addition of a stock screener using Ben Grahm's method of stock screening from Security Analysis.

# Purpose: 
I developed this code as a way to easily screen stocks then check the fundamentals of a companies stock based on its competitors. Additionally, this code was written to reinforce python data structures and visualizations.


# Methods

Allow user to input ticker of interest. 

Using Polygon API get similar tickers and remove EFTS and Mutual Funds 

Create a dictionary of classess for each ticker with information taken from YFinance API 
  -Market Cap 
  -Earnings & Revenue 
  -Price to Book , PE Ratio, PEG Ratio, Price to book 
  -Price History

Plot data against other tickers to visualize differences. 

# Learnings: 
The multiple bar graph plot in plotly needed to be in certain format. Created multilevel indexed dataframe and transposed for ease of use with plotly. 

Using a dictonary of classes to keep track of all ticker attributes prevented multiple API calls throughout code. 

Indexing through dataframes and updating dataframes. 
