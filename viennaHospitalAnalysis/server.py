import json
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
import seaborn as sns
from urllib.request import urlopen
import matplotlib.dates as mdates

workingDirectory = Path(__name__).resolve().parent
birthsDeathsAnnualDf = pd.read_csv(f"{workingDirectory}/annual_deaths_by_clinic.csv")
birthsDeathsMonthlyDf = pd.read_csv(f"{workingDirectory}/monthly_deaths.csv")
# column names and types
print(birthsDeathsAnnualDf.info())
print(birthsDeathsMonthlyDf.info())
birthsDeathsMonthlyDf['date'] = pd.to_datetime(birthsDeathsMonthlyDf['date'])
# shape of deathsByClinchDf
print(birthsDeathsAnnualDf.shape)
print(birthsDeathsMonthlyDf.shape)

# All years in the dataset: 1841 - 1846
print(f"Years in Annual Data Set: {" ,".join(birthsDeathsAnnualDf['year'].astype(str))}")

# No NaN or Duplicate values in annual data set
print(birthsDeathsAnnualDf.isna())
print(birthsDeathsAnnualDf.duplicated())

# No NaN or Duplicate values in monthly data set
print(birthsDeathsMonthlyDf.isna())
print(birthsDeathsMonthlyDf.duplicated())
birthsDeathsByMonth = birthsDeathsMonthlyDf.groupby('date').sum()

# # Avg # births per month
print(f"Avg Numbers of births per month: {round(birthsDeathsByMonth['births'].mean(),2)}")
# # Avg # deaths per month
print(f"Avg Numbers of deaths per month: {round(birthsDeathsByMonth['deaths'].mean(),2)}")

# # perecentage of women dying in hospital
births1940s = birthsDeathsAnnualDf['births'].sum()
deaths1940s = birthsDeathsAnnualDf['deaths'].sum()
print(f"% of women dying in hospital in the 1940s: {round((deaths1940s/births1940s)*100,2)}%")

# set double axis line plot to chart births and deaths
# birthsDeathsMonthAxis = birthsDeathsMonthlyDf.set_index('date')
# ax = birthsDeathsMonthAxis['births'].plot(figsize=(12, 6), legend=True, color='skyblue', linewidth=3)
# birthsDeathsMonthAxis['deaths'].plot(secondary_y=True, ax=ax,figsize=(12, 6), legend=True, linestyle='--', color='crimson', linewidth=2)

# plt.title('Births and Deaths in clinics (1940s)')
# ax.set_ylabel('births')
# ax.right_ax.set_ylabel('deaths')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator()) 
# ax.grid(True, linestyle='--')
# # rotate labels to match your example
# plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# plt.tight_layout()
# plt.show()

# Births By Clinic By Year
# for label, group in birthsDeathsAnnualDf.set_index('year').groupby('clinic'):
#     group['births'].plot(label=label)
# plt.legend()
# plt.xlabel("year")
# plt.ylabel("Births")
# plt.title("Births By Clinic By Year")
# plt.tight_layout()
# plt.show()

# Deaths By Clinic By Year
# for label, group in birthsDeathsAnnualDf.set_index('year').groupby('clinic'):
#     group['deaths'].plot(label=label)
# plt.legend()
# plt.xlabel("year")
# plt.ylabel("Deaths")
# plt.title("Deaths By Clinic By Year")
# plt.tight_layout()
# plt.show()


birthsDeathsAnnualDf['pct_deaths'] = round((birthsDeathsAnnualDf['deaths'] / birthsDeathsAnnualDf['births']) * 100, 2)

# Average Maternal Death Rates
# Average Maternal Death Rate for Clinics 1 and 2
# avgMaternalDeathRatesAnnual = birthsDeathsAnnualDf.groupby('clinic').agg({'pct_deaths':'mean'})
# print(f"Average Maternal Death Rate For Clinic 1: {round(avgMaternalDeathRatesAnnual.loc['clinic 1']['pct_deaths'], 2)}")
# print(f"Average Maternal Death Rate For Clinic 2: {round(avgMaternalDeathRatesAnnual.loc['clinic 2']['pct_deaths'], 2)}")
# clinic1Pcts = birthsDeathsAnnualDf[birthsDeathsAnnualDf['clinic'] == 'clinic 1'].set_index('year')
# print(clinic1Pcts)
# clinic2Pcts = birthsDeathsAnnualDf[birthsDeathsAnnualDf['clinic'] == 'clinic 2'].set_index('year')
# print(clinic2Pcts)

# for label, group in birthsDeathsAnnualDf.set_index('year').groupby('clinic'):
#     group['pct_deaths'].plot(label=label)
    
# plt.legend()
# plt.xlabel("year")
# plt.ylabel("Percent deaths")
# plt.title("Percent Deaths of Clinic By Year")
# plt.tight_layout()
# plt.show()

# Effects of handwashing
birthsDeathsMonthlyDf['pct_deaths'] = round((birthsDeathsMonthlyDf['deaths'] / birthsDeathsMonthlyDf['births']) * 100,2)
pre07_1947BirthDeath = birthsDeathsMonthlyDf[birthsDeathsMonthlyDf['date'] < '1847-07-01']
post07_1947BirthDeath = birthsDeathsMonthlyDf[birthsDeathsMonthlyDf['date'] >= '1847-07-01']
print(pre07_1947BirthDeath)
print(post07_1947BirthDeath)

print(f"Average Death Rate pre-June 1847: {round(pre07_1947BirthDeath['pct_deaths'].mean(),2)}")
print(f"Average Death Rate post-June 1847: {round(post07_1947BirthDeath['pct_deaths'].mean(),2)}")

# 6 month rolling average prior to handwashing
pre07_1947AvgDeath = pre07_1947BirthDeath.set_index('date')['pct_deaths'].rolling(window=6).mean()
axAvgDeath = pre07_1947AvgDeath.plot(
    figsize=(12, 6),
    legend=True,
    color='crimson',
    linestyle="--",
    linewidth=3
)
pre07_1947BirthDeath.set_index('date')['pct_deaths'].plot(
    figsize=(12, 6),
    ax=axAvgDeath,
    legend=True,
    color='grey',
    linestyle="--",
    linewidth=1
)
post07_1947BirthDeath.set_index('date')['pct_deaths'].plot(
    figsize=(12, 6),
    ax=axAvgDeath,
    legend=True,
    color='skyblue',
    linewidth=1,
    marker='o',
    markersize=8,
    markerfacecolor='blue'
)
axAvgDeath.legend(['6m Moving Average', 'Before Handwashing', 'Post Handwashing'])
axAvgDeath.xaxis.set_major_locator(mdates.YearLocator())
axAvgDeath.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
axAvgDeath.xaxis.set_minor_locator(mdates.MonthLocator()) 
plt.setp(axAvgDeath.get_xticklabels(), rotation=45, ha='right')
axAvgDeath.grid(True, linestyle='--')
axAvgDeath.plot()
plt.xlabel("Year")
plt.ylabel("Percentage of Deaths")
plt.title("Percentage of Monthly Deaths Over TIme")
plt.show()
