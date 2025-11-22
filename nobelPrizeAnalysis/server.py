import json
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
from urllib.request import urlopen


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

# plt.figure(figsize=(16,8), dpi=200)
# plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(ticks=np.arange(1900, 2021, step=5), 
#     fontsize=14, 
#     rotation=45
# )

# ax1 = plt.gca()
# ax1 = ax1.twinx()
# ax2 = ax1.twinx() 

# ax1.set_xlim(1900, 2020)
# ax2.invert_yaxis()
 
# ax1.scatter(x=prizesPerYear.index, 
#     y=prizesPerYear.values, 
#     c='dodgerblue',
#     alpha=0.7,
#     s=100
# )

# ax1.plot(prizesPerYear.index, 
#     movingAvgPricesPerYear.values, 
#     c='crimson', 
#     linewidth=3
# )

# ax2.plot(prizesPerYear.index, 
#     shareMovingAvg.values, 
#     c='grey', 
#     linewidth=3
# )
 
# plt.show()

# Top 20 Country Ranking
print(nobelPrizeDf)
top20_countries = nobelPrizeDf.groupby('birth_country_current').agg({"prize":"count"})
top20_countries.sort_values('prize', ascending=True, inplace=True)
top20_countries = top20_countries[-20:]

# plt.figure(figsize=(14,8))
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
# plt.ylabel('Prizes Awarded', fontsize=14)
# plt.xlabel('Countries', fontsize=14)
# print(top20_countries.index)
# print(top20_countries.values)
# plt.barh(top20_countries.index, top20_countries.values.flatten())
# plt.show()

top20_countriesISO = nobelPrizeDf.groupby(['birth_country_current', 'ISO'], as_index=False
).agg({'prize':'count'})
print(top20_countriesISO)
top20_countriesISO.sort_values('prize', ascending=False)
worldMap = px.choropleth(
    top20_countriesISO, 
    locations="ISO",
    color="prize",
    hover_name="birth_country_current", 
    color_continuous_scale=px.colors.sequential.matter
)
# worldMap.update_layout(coloraxis_showscale=True,)
# worldMap.show()

#category breakdown by country
top20Count_byCategory = nobelPrizeDf.groupby(['birth_country_current', 'category'], as_index=False).agg({'prize':'count'})
top20Count_byCategory.sort_values('prize', ascending=False, inplace=True)
print(top20Count_byCategory)

mergedDf = pd.merge(top20Count_byCategory, top20_countriesISO, on='birth_country_current')
print(mergedDf)
# rename the columns to make it easier to read
# mergedDf.columns = ['birth_country_current', 'category', 'cat_prize', 'ISO', 'total_prize']
# mergedDf.sort_values(by='total_prize', inplace=True)
# print(mergedDf)

# categoryCountryBar = px.bar (
#     x=mergedDf['cat_prize'],
#     y=mergedDf['birth_country_current'],
#     color=mergedDf['category'],
#     orientation='h',
#     title='Top 20 Countries by Number of Prizes and Category'
# )
# categoryCountryBar.update_layout(xaxis_title='Number of Prizes', 
#                             yaxis_title='Country')
# categoryCountryBar.show()


# Research Locations
groupedByResearchLocs = nobelPrizeDf.groupby('organization_name').agg({"prize":"count"})
groupedByResearchLocs.sort_values('prize', ascending=True, inplace=True)
top20 = groupedByResearchLocs[-20:]

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Organizations ', fontsize=14)
plt.xlabel('Number of Prizes', fontsize=14)
plt.barh(top20.index, top20.values.flatten())
plt.show()

top20BirthCities = nobelPrizeDf['organization_city'].value_counts()[:20]
top20BirthCities.sort_values(ascending=True, inplace=True)
top20BirthCitiesBar = px.bar(x = top20BirthCities.values,
    y = top20BirthCities.index,
    orientation='h',
    color=top20BirthCities.values,
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Which Cities Do the Most Research?'
)

top20BirthCitiesBar.update_layout(xaxis_title='Number of Prizes', 
                        yaxis_title='City',
                       coloraxis_showscale=False)
top20BirthCitiesBar.show()

top20BirthCities = nobelPrizeDf['birth_city'].value_counts()[:20]
top20BirthCities.sort_values(ascending=True, inplace=True)
top20BirthCitiesBar = px.bar(x = top20BirthCities.values,
    y = top20BirthCities.index,
    orientation='h',
    color=top20BirthCities.values,
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Where were the Nobel Laureates Born?'
)

top20BirthCitiesBar.update_layout(xaxis_title='Number of Prizes', 
    yaxis_title='City of Birth',
    coloraxis_showscale=False
)
top20BirthCitiesBar.show()

countryCityOrg = nobelPrizeDf.groupby(['organization_country','organization_city','organization_name'], as_index=False).agg({'prize':'count'})
countryCityOrg.sort_values('prize', ascending=False)
print(countryCityOrg)

burst = px.sunburst(
    countryCityOrg, 
    path=['organization_country', 'organization_city', 'organization_name'], 
    values='prize',
    title='Where do Discoveries Take Place?',
)

burst.update_layout(
    xaxis_title='Number of Prizes', 
    yaxis_title='City',
    coloraxis_showscale=False
)
 
burst.show()