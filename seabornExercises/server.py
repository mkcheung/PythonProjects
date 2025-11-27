import json
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
import seaborn as sns
from urllib.request import urlopen

titanicDF = pd.read_csv("titanic.csv")

# Joint Plot
# sns.jointplot(x='fare', y='age', data=titanicDF)

# Distribution Plot
# sns.distplot(titanicDF['fare'], kde=False)

# Box Plot
# sns.boxplot(x='class', y='age', data=titanicDF, hue='class')


# Swarm Plots
# sns.swarmplot(x='class', y='age', data=titanicDF, hue='class')

# Bar Plot
# titanicGroupedBySexDF = titanicDF.groupby('sex').agg({'sex':'count'})
# sns.barplot(x=titanicGroupedBySexDF.index, y='sex', data=titanicGroupedBySexDF, hue='sex')

# Matrix Grid
# titanicNumsBoolsDF = titanicDF.drop(['sex', 'embarked', 'class', 'who', 'deck', 'embark_town', 'alive'], axis=1)
# titanicNumsBoolsDFCorr = titanicNumsBoolsDF.corr()
# print(titanicNumsBoolsDFCorr.corr())
# sns.heatmap(titanicNumsBoolsDFCorr)

# FacetGrid
histogBySex = sns.FacetGrid(data=titanicDF, col='sex')
histogBySex.map(plt.hist, 'age')
plt.show()