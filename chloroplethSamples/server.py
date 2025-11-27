import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import plotly.graph_objs as go
import plotly.io as pio 
pio.renderers.default = "browser"

# data = dict(type = 'choropleth',
#             colorscale = 'Portland',
#             locationmode = 'USA-states',
#             locations = ['AZ', 'CA', 'NY'],
#             text = ['text 1', 'text 2', 'text 3'],
#             z = [1.0, 2.0, 3.0],
#             colorbar = {'title':'Colorbar Title Goes Here'}
# )

# layout = dict(geo={'scope':'usa'})
# choromap = go.Figure(data = [data], layout=layout)
# choromap.show()

df = pd.read_csv('2011_US_AGRI_Exports')
data = dict(type = 'choropleth',
            colorscale = 'YlOrRd',
            locationmode = 'USA-states',
            locations = df['code'],
            text = df['text'],
            marker = dict(line = dict(color='rgb(255,255,255)', width=2)),
            z = df['total exports'],
            colorbar = {'title':'Millions USD'}
)

layout = dict(title='2011 US Agriculture Exports by State',
              geo=dict(
                  scope='usa', 
                  showlakes=True, 
                  lakecolor='rgb(85, 173, 240)'
                )
)
choromap2 = go.Figure(data = [data], layout=layout)
choromap2.show()