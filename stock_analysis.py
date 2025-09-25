# stock_analysis.py
# Stock Market Analysis for TCS, Infosys, and Wipro (2014–2019)

# Install yfinance before running (only once in your environment):
# pip install yfinance

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

# Define start and end dates
start = "2014-01-01"
end = "2019-01-01"

# Download stock data
tcs = yf.download('TCS.NS', start=start, end=end)       # TCS India NSE
infy = yf.download('INFY.NS', start=start, end=end)     # Infosys
wipro = yf.download('WIPRO.NS', start=start, end=end)   # Wipro

# -------------------------
# 1. Volume Analysis
# -------------------------
plt.figure(figsize=(15,7))
tcs['Volume'].plot(label='TCS')
infy['Volume'].plot(label='Infosys')
wipro['Volume'].plot(label='Wipro')
plt.title('Volume of Stock Traded')
plt.legend()
plt.show()

# -------------------------
# 2. Market Capitalisation
# -------------------------
tcs['MarketCap'] = tcs['Open'] * tcs['Volume']
infy['MarketCap'] = infy['Open'] * infy['Volume']
wipro['MarketCap'] = wipro['Open'] * wipro['Volume']

plt.figure(figsize=(15,7))
tcs['MarketCap'].plot(label='TCS')
infy['MarketCap'].plot(label='Infosys')
wipro['MarketCap'].plot(label='Wipro')
plt.title('Market Capitalisation')
plt.legend()
plt.show()

# -------------------------
# 3. Volatility (Daily Returns)
# -------------------------
tcs['Returns'] = tcs['Close'].pct_change()
infy['Returns'] = infy['Close'].pct_change()
wipro['Returns'] = wipro['Close'].pct_change()

plt.figure(figsize=(15,7))
tcs['Returns'].hist(bins=100, label='TCS', alpha=0.5)
infy['Returns'].hist(bins=100, label='Infosys', alpha=0.5)
wipro['Returns'].hist(bins=100, label='Wipro', alpha=0.5)
plt.title('Stock Returns Distribution (Volatility)')
plt.legend()
plt.show()
