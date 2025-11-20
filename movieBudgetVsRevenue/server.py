import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

workingDirectory = Path(__name__).resolve().parent;
costRevenueDf = pd.read_csv(f"{workingDirectory}/cost_revenue_dirty.csv");
# 5391 rows, 6 columns
print(costRevenueDf.shape) 

# does this DF contain a NaN?
containsNaN = costRevenueDf.isna().any().any()
print(containsNaN) # data has no NaN 'inputs'

containsDuplicates = costRevenueDf.duplicated().any()
print(containsDuplicates) # df has no duplicate rows

# print(costRevenueDf.info())

#Challenge 2: Convert the USD_Production_Budget, USD_Worldwide_Gross, and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,.
costRevenueDf['USD_Production_Budget'] = costRevenueDf['USD_Production_Budget'].astype(str).str.replace("$","")
costRevenueDf['USD_Production_Budget'] = costRevenueDf['USD_Production_Budget'].astype(str).str.replace(",","")
costRevenueDf['USD_Production_Budget'] = pd.to_numeric(costRevenueDf['USD_Production_Budget'])

costRevenueDf['USD_Worldwide_Gross'] = costRevenueDf['USD_Worldwide_Gross'].astype(str).str.replace("$", "")
costRevenueDf['USD_Worldwide_Gross'] = costRevenueDf['USD_Worldwide_Gross'].astype(str).str.replace(",", "")
costRevenueDf['USD_Worldwide_Gross'] = pd.to_numeric(costRevenueDf['USD_Worldwide_Gross'])

costRevenueDf['USD_Domestic_Gross'] = costRevenueDf['USD_Domestic_Gross'].astype(str).str.replace("$", "")
costRevenueDf['USD_Domestic_Gross'] = costRevenueDf['USD_Domestic_Gross'].astype(str).str.replace(",", "")
costRevenueDf['USD_Domestic_Gross'] = pd.to_numeric(costRevenueDf['USD_Domestic_Gross'])

#Challenge 3 Convert the Release_Date column to a Pandas Datetime type.
costRevenueDf['Release_Date'] = pd.to_datetime(costRevenueDf['Release_Date'])

#Average Production Value
print(costRevenueDf)
avgProdValue = round(costRevenueDf['USD_Production_Budget'].mean(),2)
print(f"Average Production Value US: ${avgProdValue}")
avgGrossRevenue = round(costRevenueDf['USD_Worldwide_Gross'].mean() ,2)
print(f"Average Gross Revenue US: ${avgGrossRevenue}")
print(f"Minimum for worldwide revenue: ${costRevenueDf['USD_Worldwide_Gross'].min()}")
print(f"Minimum for domestic revenue: ${costRevenueDf['USD_Domestic_Gross'].min()}")

highestProdValue = round(costRevenueDf['USD_Production_Budget'].max(),2)
lowestProdValue = round(costRevenueDf['USD_Production_Budget'].min(),2)
highestGrossValue = round(costRevenueDf['USD_Worldwide_Gross'].max(),2)
print(f"Highest Production Value: ${highestProdValue}")
print(f"Highest Grossing Value: ${highestGrossValue}")

dataOfHighestProductionFilm = costRevenueDf[costRevenueDf['USD_Production_Budget'] == highestProdValue]
# print(dataOfHighestProductionFilm)
print(f"Revenue for highest budget film {dataOfHighestProductionFilm['Movie_Title']}: ${dataOfHighestProductionFilm['USD_Worldwide_Gross']}")

dataOfLowestProductionFilm = costRevenueDf[costRevenueDf['USD_Production_Budget'] == lowestProdValue]
print(f"Revenue for lowest budget film {dataOfLowestProductionFilm['Movie_Title']}: ${dataOfLowestProductionFilm['USD_Worldwide_Gross']}")

# On Films that grossed nothing domestically
print(costRevenueDf)
zeroDomesticGrossingFilmsDf = costRevenueDf[costRevenueDf['USD_Domestic_Gross'] == 0]
print(f"Number of films with a Domestic grossing of $0.00: {len(zeroDomesticGrossingFilmsDf)}")
zeroDomesticGrossingFilmsSortedDf = zeroDomesticGrossingFilmsDf.sort_values('USD_Production_Budget', ascending=False)
print(zeroDomesticGrossingFilmsSortedDf)

# On Films that grossed nothing worldwide
zeroWorldwideGrossingFilmsDf = costRevenueDf[costRevenueDf['USD_Worldwide_Gross'] == 0]
print(f"Number of films with a Worldwide grossing of $0.00: {len(zeroWorldwideGrossingFilmsDf)}")
zeroWorldwideGrossingFilmsDfSortedDf = zeroWorldwideGrossingFilmsDf.sort_values('USD_Production_Budget', ascending=False)
print(zeroWorldwideGrossingFilmsDfSortedDf)

# international releases with worldwide revenue but zero local in the US
int_wwrev_zero_local_df = costRevenueDf.query("USD_Worldwide_Gross > 0 and USD_Domestic_Gross == 0")
print(int_wwrev_zero_local_df)

# international releases with worldwide revenue but zero local in the US
query_dateTime = pd.Timestamp('2018-05-01 00:00:00')
filmsUnreleasedByMay1st2018 = costRevenueDf.query("Release_Date >= @query_dateTime")
print(filmsUnreleasedByMay1st2018)

#get a set of data that has none of these unscreened films by that time
filmsToMay1st2018Df = costRevenueDf.drop(filmsUnreleasedByMay1st2018.index)
print(filmsToMay1st2018Df)
print(f"Total Films: {len(filmsToMay1st2018Df)}")

notBreakEvenFilmsDf = filmsToMay1st2018Df.query("USD_Production_Budget > (USD_Worldwide_Gross)")
print(f"Number of Films that didn't break even: {len(notBreakEvenFilmsDf)}")
percentDidNotBreakEven = (len(notBreakEvenFilmsDf) / len(filmsToMay1st2018Df)) * 100.0
print(f"Percent of films that didn't break even: {round(percentDidNotBreakEven,2)}%")

# plt.figure(figsize=(8,4), dpi=200)
 
# ax = sns.scatterplot(data=filmsToMay1st2018Df,
#     y='USD_Production_Budget', 
#     x='Release_Date',
#     hue='USD_Worldwide_Gross',
#     size='USD_Worldwide_Gross'
# )
# ax.set(ylim=(0, 450000000),
#     xlim=(filmsToMay1st2018Df.Release_Date.min(), filmsToMay1st2018Df.Release_Date.max()),
#     xlabel='Year',
#     ylabel='Budget in $100 millions'
# )
# plt.show()
print(filmsToMay1st2018Df.info())
filmsToMay1st2018Df['Decade'] = filmsToMay1st2018Df['Release_Date'].dt.year//10*10
print(filmsToMay1st2018Df)

oldFilmsDf = filmsToMay1st2018Df[filmsToMay1st2018Df['Decade'] < 1970]
newFilmsDf = filmsToMay1st2018Df[filmsToMay1st2018Df['Decade'] >= 1970]
oldFilmsDf.sort_values('USD_Production_Budget', ascending=False, inplace=True)
print(oldFilmsDf)
print(f"Number of films prior to 1970: {len(oldFilmsDf)}")
print(f"Most expensive film made prior to 1970: {oldFilmsDf['Movie_Title'].iloc[0]}")
X = pd.DataFrame(oldFilmsDf, columns=['USD_Production_Budget'])
Y = pd.DataFrame(oldFilmsDf, columns=['USD_Worldwide_Gross'])
regression = LinearRegression()
regression.fit(X,Y)
print(f"Theta: {regression.intercept_} - Theta One: {regression.coef_}")
print(f"R-Squared: {regression.score(X, Y)}")

# linear regression plot for old films prior to 1970s
# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("whitegrid"):
#     sns.regplot(data=oldFilmsDf,
#         y='USD_Production_Budget', 
#         x='USD_Worldwide_Gross',
#         scatter_kws = {'alpha': 0.4},
#         line_kws = {'color': 'black'}
# )
# plt.show()

# linear regression plot for new films post 1970s
# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("darkgrid"):
#     ax = sns.regplot(data=newFilmsDf,
#         y='USD_Production_Budget', 
#         x='USD_Worldwide_Gross',
#         color='#2f4b7c',
#         scatter_kws = {'alpha': 0.3},
#         line_kws = {"color":"#ff7c43"})
# ax.set(
#     ylim=(0, 300000000),
#     xlim=(0, 450000000),
#     xlabel=('Revenue in $ billions'),
#     ylabel=('Budget in $100 millions')
# )
# plt.show()

X = pd.DataFrame(newFilmsDf, columns=['USD_Production_Budget'])
Y = pd.DataFrame(newFilmsDf, columns=['USD_Worldwide_Gross'])
regression = LinearRegression()
regression.fit(X,Y)

print(f"Theta: {regression.intercept_} - Theta One: {regression.coef_}")
print(f"R-Squared: {regression.score(X, Y)}")