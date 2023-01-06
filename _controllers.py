from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

# Números de Borough para nome do distrito: Manhattan (1), Bronx (2), Brooklyn (3), Queens (4), and Staten Island (5)
list_of_locations = {
    'Todos': 0,
    'Manhattan': 1,
    'Bronx': 2,
    'Brooklyn': 3,
    'Queens': 4,
    'Staten Island': 5
}

slider_size = [100, 500, 1000, 10000, 100000]

variable_dict = {'Ano de construção': 'YEAR BUILT', 'Unidades totais': 'TOTAL UNITS', 'Preço de venda': 'SALE PRICE'}

controllers = dbc.Row([
    html.Img(id='logo', src=app.get_asset_url('logo_projeto.png'), style={'width': '100%', 'margin-top': '10px'}),
    html.H3('Venda de imóveis - NYC', style={'margin-top': '30px', 'color': 'white'}),
    html.P('Utilize este dashboard para analisar as vendas ocorridas na cidade de Nova Iorque no período de 1 ano.'),
    html.H4('Distrito', style={'margin-top': '50px', 'color': 'white'}),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': i, 'value': j} for i, j in list_of_locations.items()],
        value=list_of_locations['Todos'], # 0
        placeholder='Selecione um distrito'
    ),
    html.H4('Metragem (m²)', style={'margin-top': '20px', 'margin-bottom': '20px', 'color': 'white'}),
    dcc.Slider(
        id='slider-square-size',
        min=0,
        max=4,
        value=0,
        marks={i: str(j) for i, j in enumerate(slider_size)},
        step=None
    ),
    html.H4('Variável de controle', style={'margin-top': '20px', 'margin-bottom': '20px', 'color': 'white'}),
    dcc.Dropdown(
        id='dropdown-color',
        options=[{'label': i, 'value': j} for i, j in variable_dict.items()],
        value='SALE PRICE'
    )
])