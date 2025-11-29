import json
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
import seaborn as sns
from urllib.request import urlopen

nineOneOneDF = pd.read_csv("911.csv")
print(nineOneOneDF.info())
# print(nineOneOneDF[nineOneOneDF['twp']=='NEW HANOVER'].loc[0]['lat'])

# What are the top 5 zipcodes for 911 calls? 
top5ZipCodesFor911 = nineOneOneDF['zip'].value_counts().head(5)
print(f"Top five zip codes for 911 calls: {", ".join(top5ZipCodesFor911.index.astype(int).astype(str))}")

# What are the top 5 townships (twp) for 911 calls? 
top5TownShipsFor911 = nineOneOneDF['twp'].value_counts().head(5)
print(f"Top five townships to 911: {", ".join(top5TownShipsFor911.index)}")

def returnReasonDepartment(title):
    titleComponents = title.split(':')
    return titleComponents[0]

def returnDate(dateTime):
    return dateTime.date()

def returnHour(dateTime):
    return dateTime.hour

def returnMonth(dateTime):
    return dateTime.month

def returnDayOfWeek(dateTime):
    dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
    return dmap[dateTime.dayofweek]

nineOneOneDF['Reason'] = nineOneOneDF['title'].apply(returnReasonDepartment)

nineOneOneReasPartitions = nineOneOneDF['Reason'].value_counts()

# What is the most common Reason for a 911 call based off of this new column?
print(f"Top reason to call 911: {nineOneOneReasPartitions.index[0]}")

# seaborn countplot of Reasons
# sns.countplot(data=nineOneOneDF, x="Reason", palette="viridis")
# plt.title("911 Call Reasons")
# plt.xlabel("Reasons")
# plt.ylabel("Count")
# plt.show()

print(nineOneOneDF)
nineOneOneDF['timeStamp'] = pd.to_datetime(nineOneOneDF['timeStamp'])
nineOneOneDF['Hour'] = nineOneOneDF['timeStamp'].apply(returnHour)
nineOneOneDF['Month'] = nineOneOneDF['timeStamp'].apply(returnMonth)
nineOneOneDF['Day Of Week'] = nineOneOneDF['timeStamp'].apply(returnDayOfWeek)

# count of reasons per day of week
# sns.countplot(data=nineOneOneDF, x="Day Of Week", hue='Reason')
# plt.title("911 Call Reasons By Day of Week")
# plt.xlabel("Day Of Week")
# plt.ylabel("Count")
# plt.show()

# count of reasons per month
# sns.countplot(data=nineOneOneDF, x="Month", hue='Reason')
# plt.title("911 Call Reasons By Month")
# plt.xlabel("Month")
# plt.ylabel("Count")
# plt.show()


nineOneOneCntByMonth = nineOneOneDF.groupby('Month').count().reset_index()
print(nineOneOneCntByMonth)

# sns.lineplot(x='Month', y='title', data=nineOneOneCntByMonth)
# plt.show()
# sns.lmplot(x='Month', y='title', data=nineOneOneCntByMonth)
# plt.show()

nineOneOneDF['Date'] = nineOneOneDF['timeStamp'].apply(returnDate)
nineOneOneEmsDF = nineOneOneDF[nineOneOneDF['Reason']=='EMS']
# nineOneOneEmsDF.groupby(['Date'])['Reason'].count().plot()

nineOneOneFireDF = nineOneOneDF[nineOneOneDF['Reason']=='Fire']
# nineOneOneFireDF.groupby(['Date'])['Reason'].count().plot()

nineOneOneTrafficDF = nineOneOneDF[nineOneOneDF['Reason']=='Traffic']
# nineOneOneTrafficDF.groupby(['Date'])['Reason'].count().plot()
plt.xticks(rotation=45)

# print(nineOneOneDF.groupby(['Day Of Week', 'Hour']).count()['Reason'])
# print(nineOneOneDF.groupby(['Day Of Week', 'Hour']).count()['Reason'].unstack())
dayVsHour = nineOneOneDF.groupby(['Day Of Week', 'Hour']).count()['Reason'].unstack()

plt.figure(figsize=(12, 6))
# sns.heatmap(dayVsHour, cmap='viridis')
# sns.clustermap(dayVsHour, cmap='viridis')


dayVsMonth = nineOneOneDF.groupby(['Day Of Week', 'Month']).count()['Reason'].unstack()

# sns.heatmap(dayVsMonth, cmap='viridis')
# sns.clustermap(dayVsMonth, cmap='viridis')

# plt.show()