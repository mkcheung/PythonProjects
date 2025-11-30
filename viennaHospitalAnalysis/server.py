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
birthsDeathsMonthAxis = birthsDeathsMonthlyDf.set_index('date')
ax = birthsDeathsMonthAxis['births'].plot(figsize=(12, 6), legend=True, color='skyblue', linewidth=3)
birthsDeathsMonthAxis['deaths'].plot(secondary_y=True, ax=ax,figsize=(12, 6), legend=True, linestyle='--', color='crimson', linewidth=2)

plt.title('Births and Deaths in clinics (1940s)')
ax.set_ylabel('births')
ax.right_ax.set_ylabel('deaths')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator()) 
ax.grid(True, linestyle='--')
# rotate labels to match your example
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()
