import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd


#################################################################################
# Tesla And Charts
workingDirectory = Path(__file__).resolve().parent;
# teslaDf = pd.read_csv(f"{workingDirectory}/TESLA Search Trend vs Price.csv")
# teslaDf.MONTH = pd.to_datetime(teslaDf.MONTH)
# print(teslaDf)
# print(teslaDf.shape)
# print(teslaDf.columns)
# print(f"Max Search Tesla: {teslaDf['TSLA_WEB_SEARCH'].max()}")
# print(f"Min Search Tesla: {teslaDf['TSLA_WEB_SEARCH'].min()}")
# print(f"Missing Values for Tesla DF: {teslaDf.isna().values.any()}")

# plt.figure(figsize=(14,8), dpi=120) 
# plt.title("Tesla Web Search vs Price")
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Search Trend', color='skyblue')
# ax2.set_ylabel('Stock Price', color='#E6232E')
# ax1.plot(teslaDf.MONTH, teslaDf.TSLA_WEB_SEARCH, color='skyblue')
# ax2.plot(teslaDf.MONTH, teslaDf.TSLA_USD_CLOSE, color='#E6232E')
# plt.show()

#################################################################################
#################################################################################
# Bitcoin
# bitcoinDf = pd.read_csv(f"{workingDirectory}/Bitcoin Search Trend.csv")
# bitcoinDf.MONTH = pd.to_datetime(bitcoinDf.MONTH)
# print(bitcoinDf)
# print(bitcoinDf.shape)
# print(bitcoinDf.columns)
# print(f"Bitcoin Search Trend Max: {bitcoinDf['BTC_NEWS_SEARCH'].max()}")
# print(f"Bitcoin Search Trend Min: {bitcoinDf['BTC_NEWS_SEARCH'].min()}")
# print(f"Missing Values for Bitcoin: {bitcoinDf.isna().values.any()}")

# dailybitcoinDf = pd.read_csv(f"{workingDirectory}/Daily Bitcoin Price.csv")
# dailybitcoinDf.DATE = pd.to_datetime(dailybitcoinDf.DATE)
# print(dailybitcoinDf)
# print(dailybitcoinDf.shape)
# print(dailybitcoinDf.columns)
# np_dailybitCoin = dailybitcoinDf.isna().values;


# # #find out where in the dataframe a value resides
# (rows, cols) = np.where(np_dailybitCoin==True)
# print(rows)
# print(cols)
# print(dailybitcoinDf.iloc[2148,1])
# print(dailybitcoinDf.iloc[2148,2])
# print(f"Missing Values for Daily Bitcoin: {dailybitcoinDf.isna().values.any()}")
# print(f"How many missing values? {dailybitcoinDf.isna().values.sum()}")
# #remove missing values
# dailybitcoinDf.dropna(inplace=True)

# # resampled
# monthlybitcoinDf = dailybitcoinDf.resample('M', on='DATE').last()
# Bitcoin And Charts - Price vs Search 
# plt.figure(figsize=(14,8), dpi=120) 
# plt.title("Bitcoin News Search vs Resampled Price")
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Search Trend', color='skyblue')
# ax2.set_ylabel('BTC Price', color='#E6232E')
# ax1.plot(bitcoinDf.MONTH, bitcoinDf.BTC_NEWS_SEARCH, color='skyblue')
# ax2.plot(monthlybitcoinDf.index, monthlybitcoinDf.CLOSE, color='#E6232E')
# plt.show()

#################################################################################
#################################################################################

ueBenefits20042019Df = pd.read_csv(f"{workingDirectory}/UE Benefits Search vs UE Rate 2004-19.csv")
ueBenefits20042019Df.MONTH = pd.to_datetime(ueBenefits20042019Df.MONTH)
print(ueBenefits20042019Df)
print(ueBenefits20042019Df.shape)
print(ueBenefits20042019Df.columns)
print(f"UE Benefits 2004 - 2019 Max Search Tesla: {ueBenefits20042019Df['UE_BENEFITS_WEB_SEARCH'].max()}")
print(f"UE Benefits 2004 - 2019 Min Search Tesla: {ueBenefits20042019Df['UE_BENEFITS_WEB_SEARCH'].min()}")
print(f"Missing Values for UE Benefits 2004 - 2019: {ueBenefits20042019Df.isna().values.any()}")

plt.figure(figsize=(14,8), dpi=120) 
plt.title("Monthly Search of \"Unemployment Benefits\" in the U.S. vs the U/E Rate")
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
ax1 = plt.gca()
ax1.grid(color='grey')
ax2 = ax1.twinx()
ax1.set_xlabel('Year')
ax1.set_ylabel('Search Trend', color='skyblue')
ax2.set_ylabel('FRED U/E Race', color='#E6232E')
ax1.plot(ueBenefits20042019Df.MONTH, ueBenefits20042019Df.UE_BENEFITS_WEB_SEARCH, color='skyblue')
ax2.plot(ueBenefits20042019Df.MONTH, ueBenefits20042019Df.UNRATE, color='#E6232E', linestyle='--')
plt.show()

#################################################################################
#################################################################################

# ueBenefits20042020Df = pd.read_csv(f"{workingDirectory}/UE Benefits Search vs UE Rate 2004-20.csv")
# ueBenefits20042020Df.MONTH = pd.to_datetime(ueBenefits20042020Df.MONTH)
# print(ueBenefits20042020Df)
# print(ueBenefits20042020Df.shape)
# print(ueBenefits20042020Df.columns)
# print(f"UE Benefits 2004 - 2020 Max Search Tesla: {ueBenefits20042020Df['UE_BENEFITS_WEB_SEARCH'].max()}")
# print(f"UE Benefits 2004 - 2020 Min Search Tesla: {ueBenefits20042020Df['UE_BENEFITS_WEB_SEARCH'].min()}")
# print(f"Missing Values for UE Benefits 2004 - 2020: {ueBenefits20042020Df.isna().values.any()}")


# plt.figure(figsize=(14,8), dpi=120) 
# plt.title("Monthly Search of \"Unemployment Benefits\" in the U.S. vs the U/E Rate")
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Search Trend', color='skyblue')
# ax2.set_ylabel('FRED U/E Race', color='#E6232E')
# ax1.plot(ueBenefits20042020Df.MONTH, ueBenefits20042020Df.UE_BENEFITS_WEB_SEARCH, color='skyblue')
# ax2.plot(ueBenefits20042020Df.MONTH, ueBenefits20042020Df.UNRATE, color='#E6232E')
# plt.show()