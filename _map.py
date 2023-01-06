from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

fig = go.Figure(

)

fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0, 0, 0, 0)')
# paper_bgcolor altera a 'bordinha' em torno do gráfico, normalmente branca

map = dbc.Row([
    dcc.Graph(id='map-graph', figure=fig)
], style={'height': '80vh'})

