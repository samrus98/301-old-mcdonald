import dash
from dash import dcc, html, Input, Output
import pandas as pd

selector_columns = ['beef', 'pork', 'poultry','dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh', 'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']
df = pd.read_csv('assets/usa-2011-agriculture.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in selector_columns],
        value=selector_columns[0]
    ),
    html.Br(),
    dcc.Graph(id='display-value')
])


@app.callback(Output('display-value', 'figure'),
              [Input('dropdown', 'value')])

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


if __name__ == '__main__':
    app.run_server(debug=True)