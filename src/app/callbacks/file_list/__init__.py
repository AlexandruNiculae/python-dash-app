from dash import Dash

from app.callbacks.file_list.file_list import register_callbacks

def register_file_list_callbacks(app: Dash)-> None:
    register_callbacks(app)
