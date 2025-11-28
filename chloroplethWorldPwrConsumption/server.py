import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import plotly.graph_objs as go
import plotly.io as pio 
pio.renderers.default = "browser"


#power consumption through the world
# df = pd.read_csv("2014_World_Power_Consumption")
# data = dict(type = 'choropleth',
#             locations = df['Country'],
#             locationmode = 'country names',
#             text = df['Text'],
#             z = df['Power Consumption KWH'],
#             colorbar = {'title':'Power Consumption KWH'}
# )
# layout = dict(title='2014 Global GDP',
#               geo=dict(
#                   showframe=False, 
#                   projection = {'type':'mercator'}
#                 )
# )
# choromap = go.Figure(data = [data], layout=layout)
# choromap.show()


# 2012 election data
df = pd.read_csv("2012_Election_Data")
print(df.info())
data = dict(type = 'choropleth',
            locations = df['State Abv'],
            locationmode = 'USA-states',
            text = df['State'],
            z = df['Voting-Age Population (VAP)'],
            colorscale='Viridis',
            colorbar = {'title':'Voting-Age Population'}
)
layout = dict(title='2012 Election Data',
              geo=dict(
                  scope='usa',
                  showlakes=True, 
                  lakecolor='rgb(85, 173, 240)',
                )
)
choromap = go.Figure(data = [data], layout=layout)
choromap.show()