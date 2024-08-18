from dash import Dash

from app.callbacks.mock_list.mock_list import register_callbacks

def register_mock_list_callbacks(app: Dash)-> None:
    register_callbacks(app)
