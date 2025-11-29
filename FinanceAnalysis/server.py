import json
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
import seaborn as sns
from urllib.request import urlopen

allBanksDF = pd.read_pickle("all_banks")

tickerSymbols = [
    'BAC',
    'C',
    'GS',
    'JPM',
    'MS',
    'WFC'
]
bacDf = allBanksDF['BAC']
cDf = allBanksDF['C']
gsDf = allBanksDF['GS']
jpmDf = allBanksDF['JPM']
msDf = allBanksDF['MS']
wfcDf = allBanksDF['WFC']

bankStocks = pd.concat([bacDf, cDf, gsDf, jpmDf, msDf, wfcDf], keys=tickerSymbols, axis=1)
bankStocks.columns.names = ['Bank Ticker','Stock Info']
# print(bankStocks['BAC']['Close'].max())
closePricesPerBank = bankStocks.xs('Close', level='Stock Info', axis=1)
# print(closePricesPerBank['BAC'])
# print(closePricesPerBank.max())
# closePricesPerBank['dailyReturn'] = closePricesPerBank[]
returnsDf = pd.DataFrame()
for symbol in tickerSymbols:
    returnsDf[f"{symbol} Return"] = closePricesPerBank[f"{symbol}"].pct_change()
# sns.pairplot(returnsDf)
print(returnsDf)
print(returnsDf.idxmin()) # dates of worst returns
print(returnsDf.idxmax()) # dates of best returns 
print(allBanksDF.loc['2011-05-06':'2011-05-10'])

# standard deviation of returns for all banks over the whole time frame
print(returnsDf.std()) 

# give me all data regarding returns in the year 2015 (index is a datetime object)
print(returnsDf.loc['2015']) 

# standard deviations of bank returns in the year 2015 (index is a datetime object)
print(returnsDf.loc['2015'].std()) 

# distplot of 2015 Morgan Stanley Returns
# sns.distplot(returnsDf.loc['2015']['MS Return'], bins=30)
# plt.tight_layout()
# plt.show()
# print(closePricesPerBank)

# line plot of bank closing prices the whole time frame of the data set
# closePricesPerBank.plot(figsize=(12,6))
# plt.title('Bank Closing Prices Over Time')
# plt.xlabel('Date')
# plt.ylabel('Closing Price (USD)')
# plt.legend(title='Bank')
# plt.tight_layout()
# plt.show()

# line plot of bank closing prices and rolling 30-day average
# bacClosingPricesFor2008 = closePricesPerBank.loc['2008']['BAC'];
# bacCPRollAvg40Days2008 = bacClosingPricesFor2008.rolling(window=30).mean()
# print(bacClosingPricesFor2008)
# print(bacCPRollAvg40Days2008)
# mergedClosedAndRolling2008Bac = pd.concat([bacClosingPricesFor2008, bacCPRollAvg40Days2008], axis=1)
# mergedClosedAndRolling2008Bac.columns = ['Closing', 'Rolling Avg']
# print(mergedClosedAndRolling2008Bac)
# mergedClosedAndRolling2008Bac.plot(figsize=(12,6))
# plt.title('BAC Closing Prices and Rolling Avg')
# plt.xlabel('Date')
# plt.ylabel('Closing Prices')
# plt.tight_layout()
# plt.show()


closePricesPerBankCorr = closePricesPerBank.corr()

plt.figure(figsize=(12, 6))
# sns.heatmap(closePricesPerBankCorr, cmap='Reds', annot=True)
sns.clustermap(closePricesPerBankCorr, cmap='Reds', annot=True)
plt.show()

