import dash
from dash import dcc
#import dash_core_components as dcc
from dash import html
#import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

# here's the list of possible columns to choose from.
list_of_columns =['code', 'state', 'category', 'total exports', 'beef', 'pork', 'poultry',
       'dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh',
       'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']
selector_columns = ['beef', 'pork', 'poultry',
       'dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh',
       'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']

#mycolumn='corn'
myheading1 = '2011 US Agriculture Exports by State'
mygraphtitle = '2011 US Agriculture Exports by State'
mycolorscale = 'PuBuGn' # Note: The error message will list possible color scales.
mycolorbartitle = "Millions USD"
tabtitle = 'Sam-dropdown'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/samrus98/301-old-mcdonald'


########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/usa-2011-agriculture.csv')



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.Dropdown(id='dropdown-mcd', options=selector_columns, value='corn'),
    dcc.Graph(id='display-value'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

@app.callback(
    Output('display-value', 'children'),
    Input('dropdown-mcd', 'value')
)

def update_output(value):
    mycolumn = value
    #myheading1 = f"Wow! That's a lot of {mycolumn}!"
    #return f'You have selected {mycolumn}'
    fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df[mycolumn].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = mycolorscale,
    colorbar_title = mycolorbartitle,
    ))

    fig.update_layout(
        title_text = mygraphtitle,
        geo_scope='usa',
        width=1200,
        height=800
    ) 
    return fig

############ Deploy
if __name__ == '__main__':
    app.run_server()