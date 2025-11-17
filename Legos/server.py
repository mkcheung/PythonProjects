import matplotlib.pyplot as plt
import os
from pathlib import Path
import pandas as pd

workingDirectory = Path(__file__).resolve().parent 
colorsDf = pd.read_csv(f"{workingDirectory}/colors.csv")
# # print(colorsDf.columns)
# # print(colorsDf.nunique())
# uniqueColors = colorsDf['name'].unique()
# # unique color names and the number
# # print(f"Number of Unique Colors: {len(uniqueColors)}")

# # number of transparent colors
# # print(colorsDf['is_trans'].unique())
# transparentColors = colorsDf[colorsDf['is_trans']=='t']
# # print(transparentColors)
# # print(f"Number of Transparent Colors: {len(transparentColors)}")
# numOpaqueColors = len(uniqueColors) - len(transparentColors)
# # print(f"Number of Opaque colors: {numOpaqueColors}")
####################################################################################

setsDf = pd.read_csv(f"{workingDirectory}/sets.csv")

setsDfSortedAsc= setsDf.sort_values(by="year")
# first lego sets were released in 1949
# Extra-Large Gift Set
# Large Gift Set
# Medium Gift Set
# Small Brick Set
# Small Doors and Windows Set
# print(setsDfSortedAsc.head(20))
####################################################################################

# first year of operation
# productsFromFirstYear = setsDfSortedAsc[setsDfSortedAsc['year']==1949]
# productNamesFromFirstYear = productsFromFirstYear['name']
# # products from first year of ops productsFromFirstYear
# print(f"Num of Products from first year of ops - 1949: {len(productsFromFirstYear)}")
# concatenatedNamesOfProducts = ', ' .join(productNamesFromFirstYear);
# print(f"Products output in from first year of ops: {concatenatedNamesOfProducts}")
####################################################################################

# Sets with the most parts
# setsMostPartsDf = setsDf.sort_values('num_parts', ascending=False);
# nameOfSetsWithMostParts = setsMostPartsDf.head(5)['name']
# concatenatedNamesOfSetsWithMostParts = " ,".join(nameOfSetsWithMostParts)

# groupedByYear = setsDf.groupby('year').count()

####################################################################################
# Exercises
themes_by_year = setsDf.groupby('year').agg({'theme_id': pd.Series.nunique})

print(themes_by_year.head(50))
themes_by_year.rename(columns = {'theme_id':'nr_themes'}, inplace = True)
themesGroupedFrom1949To2019 = themes_by_year.loc[1949:2019]

# ax1 = plt.gca()
# ax2 = ax1.twinx()

# ax1.plot(groupedByYear.index[:-2], groupedByYear.set_num[:-2], color='g')
# ax2.plot(themesGroupedFrom1949To2019.index[:-2],themesGroupedFrom1949To2019.nr_themes[:-2], color='b')

# ax1.set_xlabel('Year')
# ax2.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of Themes', color='blue')
# plt.show()
####################################################################################

# Scatter Plots
# parts_per_set = setsDf.groupby('year').agg({'num_parts':'mean'})
# print(parts_per_set)
# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.xlabel('Year')
# plt.ylabel('Avg Parts')
# plt.show()

####################################################################################

themesDf = pd.read_csv(f"{workingDirectory}/themes.csv")
# groupedByStarWars = themesDf.groupby('name').agg({'id':'count'})
# print(groupedByStarWars.head(150))
####################################################################################


set_theme_count = setsDf["theme_id"].value_counts()[:10]
print(set_theme_count)
# reconstruct series into data frame
set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                                'set_count':set_theme_count.values})

merged_df = pd.merge(set_theme_count, themesDf, on="id")
print(merged_df[:3])
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()