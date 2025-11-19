import matplotlib.pyplot as plt
import os
from pathlib import Path
import pandas as pd
import plotly.express as px

workingDirectory = Path(__name__).resolve().parent;
appsDf = pd.read_csv(f"{workingDirectory}/apps.csv");

#10841 rows
#12 columns
print(appsDf.shape)
print(appsDf.columns)
print(appsDf.sample())

# drop two columns
appsDf.drop(columns=['Last_Updated', 'Android_Ver'], inplace=True)
print(appsDf.sample())

# how many rows have NaN in Rating Column?
# check for NaN using isna() method
# tally with sum() method
print(appsDf['Rating'].isna().sum())

#specific rows with NaN in Rating
print(appsDf[appsDf['Rating'].isna()])
df_apps_clean = appsDf[~appsDf['Rating'].isna()]
print(df_apps_clean)

#highest rated apps
apps_sorted_rating_desc = df_apps_clean.sort_values('Rating', ascending=False)
rated_five_apps = apps_sorted_rating_desc[apps_sorted_rating_desc['Rating']==5.0]
print(f"Apps rated at five stars: {" ,".join(rated_five_apps['App'].astype(str).tolist())}")

#Largest Apps 
appsSortedBySizeDF = appsDf.sort_values('Size_MBs', ascending=False)
print(appsSortedBySizeDF[['App', 'Size_MBs']].head(50))

#Apps With greatest numbrer of reviews
appsSortedByNumReviews = appsDf.sort_values('Reviews', ascending=False)
print(appsSortedByNumReviews[['App', 'Reviews', 'Type']])

# aggregating all values by content rating
ratingsAggregated = df_apps_clean['Content_Rating'].value_counts()
print(ratingsAggregated)
pieChart = px.pie(
    labels = ratingsAggregated.index, 
    values = ratingsAggregated.values,
    title="Content Ratings",
    names=ratingsAggregated.index,
    hole=0.6
)
pieChart.update_traces(textposition='outside', textinfo='percent+label')
# pieChart.show()

#Installations 
print(df_apps_clean['Installs'].describe())
df_apps_clean['Installs'] = df_apps_clean['Installs'].astype(str).str.replace(",","")
df_apps_clean['Installs'] = pd.to_numeric(df_apps_clean['Installs'])
groupedByInstalls = df_apps_clean[['App', 'Installs']].groupby('Installs').count()
print(groupedByInstalls)

print(df_apps_clean)
df_apps_clean['Price'] = df_apps_clean['Price'].astype(str).str.replace("$","")
df_apps_clean['Price'] = pd.to_numeric(df_apps_clean['Price'])
print(df_apps_clean[['App', 'Price']])

df_items_greater_350 = df_apps_clean[df_apps_clean['Price'] > 250.0]
df_apps_clean = df_apps_clean[df_apps_clean['Price'] <= 250.0]
print(df_apps_clean.sort_values('Price', ascending=False))


df_apps_clean['Revenue_Estimate'] = df_apps_clean['Installs'] * df_apps_clean['Price']
rev_estimate_sorted = df_apps_clean.sort_values('Revenue_Estimate', ascending=False)
print(rev_estimate_sorted[['App', 'Installs', 'Price', 'Revenue_Estimate']])
df_apps_clean.Category.nunique()
# Competitive Apps and Popular Categories

topten_categories = df_apps_clean['Category'].value_counts()[:10]
print('----------------top ten categories----------------')
print(topten_categories)
print('----------------top ten categories----------------')
barchart = px.bar(x=topten_categories.index, y= topten_categories.values)
# barchart.show()

# installations per category
categoriesToInstallations = df_apps_clean.groupby('Category').agg({'Installs':'sum'})
categoriesToInstallations.sort_values('Installs', ascending=False, inplace=True)
# print(categoriesToInstallations)

h_barchart = px.bar(
    x=categoriesToInstallations.Installs,
    y=categoriesToInstallations.index,
    orientation='h',
    title="Categories To Installations")

h_barchart.update_layout(
    xaxis_title="Number of Installations",
    yaxis_title="Categories"
)

# h_barchart.show()

# categories to installs aand number of apps 
catToInstallsAndNumApps = df_apps_clean.groupby('Category').agg({'Installs':'sum', 'App':'count'}).sort_values('Installs', ascending=False)

print(catToInstallsAndNumApps)
scatter = px.scatter(
    catToInstallsAndNumApps, 
    x='App', 
    y='Installs',
    title="Category Installations",
    size='App'
)

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
# scatter.show()


# print(df_apps_clean['Genres'].value_counts())
# stackedItems = df_apps_clean['Genres'].str.split(';', expand=True).stack()
# numGenres = stackedItems.value_counts()
# print(numGenres)
# genres_barchart = px.bar(
#     x=numGenres.index[:15],
#     y= numGenres.values[:15],
#     title="Top Genres",
#     hover_name=numGenres.index[:15],
#     color=numGenres.values[:15],
#     color_continuous_scale='Agsunset'
# )

# genres_barchart.update_layout(
#     xaxis_title="Genre",
#     yaxis_title="Number of Apps",
#     coloraxis_showscale=False
# )
# genres_barchart.show()
groupedByTypesCats = df_apps_clean.groupby(['Category', 'Type'], as_index=False).agg({'App':pd.Series.count})
print(groupedByTypesCats.sort_values('App', ascending=True).head())

#grouped bar charts
# g_bar = px.bar(groupedByTypesCats,
#     x='Category',
#     y='App',
#     title='Free vs Paid Apps by Category',
#     color='Type',
#     barmode='group'
# )
 
# g_bar.update_layout(xaxis_title='Category',
#     yaxis_title='Number of Apps',
#     xaxis={'categoryorder':'total descending'},
#     yaxis=dict(type='log')
# )

# g_bar.show()

# box plots

groupedTotalsInstalls = df_apps_clean.groupby(['Category', 'Type'], as_index=False).agg({'Installs':pd.Series.sum})
print(groupedTotalsInstalls.sort_values('Installs', ascending=True).head())
fig = px.box(
    groupedTotalsInstalls,
    y="Installs",
    x="Type",
    color='Type',
    notched=True,
    points='all',
    title='How Many Downloads are Paid Apps Giving Up?'
)
fig.show()