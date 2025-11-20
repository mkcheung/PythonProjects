import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

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