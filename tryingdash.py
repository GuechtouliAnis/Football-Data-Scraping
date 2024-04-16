import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Sample data (population of some countries)
country_population = {
    'USA': 331002651,
    'China': 1439323776,
    'India': 1380004385,
    'Brazil': 212559417,
    'Pakistan': 220892340
}

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Country Population Dashboard"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[
            {'label': country, 'value': country} for country in country_population.keys()
        ],
        value='USA'
    ),
    html.Div(id='population-output'),
    dcc.Graph(id='population-graph')
])

# Define callback to update population and graph when country is selected
@app.callback(
    [Output('population-output', 'children'),
     Output('population-graph', 'figure')],
    [Input('country-dropdown', 'value')]
)
def update_population_and_graph(selected_country):
    population = country_population.get(selected_country, 'N/A')
    
    # Create bar graph data
    data = [go.Bar(
        x=list(country_population.keys()),
        y=list(country_population.values()),
        marker=dict(color='blue')
    )]
    
    # Create bar graph layout
    layout = go.Layout(
        title="Population of Countries",
        xaxis=dict(title='Country'),
        yaxis=dict(title='Population')
    )
    
    return f"Population of {selected_country}: {population:,}", {'data': data, 'layout': layout}


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
