import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd
import plotly.express as px

workingDirectory = Path(__file__).resolve().parent
nobelPrizeDf = pd.read_csv(f"{workingDirectory}/nobel_prize_data.csv")
# 16 Columns, 962 Rows
print(nobelPrizeDf.shape) 
print(nobelPrizeDf.info())
nobPrizes_ascYear_Df = nobelPrizeDf.sort_values('year', ascending=True)
nobPrizes_descYear_Df = nobelPrizeDf.sort_values('year', ascending=False)
print(f"Year Of First Nobel Prize: {nobPrizes_ascYear_Df['year'].iloc[0]}")
print(f"Year of Latest Nobel Prize: {nobPrizes_descYear_Df['year'].iloc[0]}")

# Any duplicates in the data set?
anyDups = nobelPrizeDf.duplicated().values.any()
print(f"Does the nobel prize dataset have any duplicate rows?: {anyDups}")

# Any NaN values in the data set?
anyNaNs = nobelPrizeDf.isna().any().any()
print(f"Does the nobel prize dataset have any Nan values?: {anyNaNs}")

# Which columns have NaN values?
colsWithNans = nobelPrizeDf.isna().any()
print(f"Does the nobel prize dataset have any Nan values?: {anyNaNs}")

#how many NaNs are in each column?
numNaNsInEachCol = nobelPrizeDf.isna().sum()
print(numNaNsInEachCol)

# view dataset with a specific subset and with rows having NaN in birthday
col_subset=['year', 'category', 'laureate_type', 'birth_date', 'full_name', 'organization_name']
print(nobelPrizeDf[nobelPrizeDf['birth_date'].isna()][col_subset])

nobelPrizeDf['birth_date'] = pd.to_datetime(nobelPrizeDf['birth_date'])
print(nobelPrizeDf.info())
prizeShareSplit = nobelPrizeDf['prize_share'].str.split('/', expand=True)
numerator = pd.to_numeric(prizeShareSplit[0])
denominator = pd.to_numeric(prizeShareSplit[1])
print(numerator)
print(denominator)
nobelPrizeDf['share_pct'] = (numerator/denominator)*100
print(nobelPrizeDf.info())

# what percentages of the prizes were given to each category
# menWomenProportions = nobelPrizeDf['category'].value_counts()
# pieChartCategories = px.pie(
#     labels = menWomenProportions.index, 
#     values = categoryProportions.values,
#     title="Categories of Nobel Prizes",
#     names=categoryProportions.index
# )
# pieChartCategories.update_traces(textposition='outside', textinfo='percent+label')
# pieChartCategories.show()

# what percentages of the prizes were given to men vs women
# menWomenProportions = nobelPrizeDf['sex'].value_counts()
# menToWomenChartCategories = px.pie(
#     labels = menWomenProportions.index, 
#     values = menWomenProportions.values,
#     title="Men To Women Recipients",
#     names=menWomenProportions.index,
#     hole=0.6
# )
# menToWomenChartCategories.update_traces(textposition='outside', textinfo='percent+label')
# menToWomenChartCategories.show()

# On Women Nobel Laureates
# womensNobelaureatesDf = nobelPrizeDf[nobelPrizeDf['sex'] == 'Female'].sort_values('year', ascending=True)
# print(womensNobelaureatesDf[['year', 'category', 'full_name', 'birth_country', 'organization_name']])
# womensNobelaureatesGroupedDF = womensNobelaureatesDf.groupby('full_name').agg({'full_name':pd.Series.count})
# print(womensNobelaureatesGroupedDF)

# Economics
# first prize in 1969, awarded to Jan Tinbergen
economicsDF = nobelPrizeDf[nobelPrizeDf['category'] == 'Economics'].sort_values('year', ascending=True)
print(economicsDF[['category', 'year', 'full_name']])

countsOfNPWinners = nobelPrizeDf.groupby('full_name').size()
multiWinners = countsOfNPWinners[countsOfNPWinners>1]
multiWinners.sort_values(ascending=False)
print(multiWinners)

# prizes per year
prizesPerYearDf = nobelPrizeDf.groupby('year').size()
print(prizesPerYearDf)


roll_prizesPerYearDf = prizesPerYearDf.rolling(window=5).mean()
x_axis_ticks = np.arange(roll_prizesPerYearDf.index.min(),2021, 5)

# plt.scatter(roll_prizesPerYearDf.index, roll_prizesPerYearDf.values, label='Nobel Prizes To Year')
# plt.legend()
# plt.xticks(x_axis_ticks, rotation=45)
# plt.xlabel('Years')
# plt.ylabel('Nobel Prizes Awarded')
# plt.title('Nobel Prizes Per Year')
# plt.show()

# averages
print(nobelPrizeDf)
prizesPerYear = nobelPrizeDf.groupby('year').agg({'prize':'count'})
movingAvgPricesPerYear = prizesPerYear.rolling(window=5).mean()
print(movingAvgPricesPerYear)

yearlyAvgShare = nobelPrizeDf.groupby(by="year").agg({'share_pct':'mean'})
shareMovingAvg = yearlyAvgShare.rolling(window=5).mean()

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), 
    fontsize=14, 
    rotation=45
)

ax1 = plt.gca()
ax1 = ax1.twinx()
ax2 = ax1.twinx() 

ax1.set_xlim(1900, 2020)
ax2.invert_yaxis()
 
ax1.scatter(x=prizesPerYear.index, 
    y=prizesPerYear.values, 
    c='dodgerblue',
    alpha=0.7,
    s=100
)

ax1.plot(prizesPerYear.index, 
    movingAvgPricesPerYear.values, 
    c='crimson', 
    linewidth=3
)

ax2.plot(prizesPerYear.index, 
    shareMovingAvg.values, 
    c='grey', 
    linewidth=3
)
 
plt.show()