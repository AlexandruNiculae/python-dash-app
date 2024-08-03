import os
os.environ['REACT_VERSION'] = '18.2.0'

from dash import Dash, dcc, html
import dash_mantine_components as dmc

from app.layouts.not_implemented import NotImplementedComponent
from config import APP_OWNER



app_temp_body = dmc.Center(
    children=[
        NotImplementedComponent().render()
    ],
)

app_base_content = dmc.MantineProvider(
    children=[
        dcc.Interval(
            id='main-one-time-interval',
            interval=1*1000,  # in milliseconds
            n_intervals=0,    # start at interval 0
            max_intervals=1   # only fire once
        ),
        dmc.Stack(id="main-container", children=[
            dmc.Title(f"{APP_OWNER}'s app", order=1),
            dmc.Divider(variant="solid"),
            html.Div(id="main-canvas", children=[
                app_temp_body
            ]),

        ]),
    ]
)

app = Dash(__name__)
app.layout = app_base_content
