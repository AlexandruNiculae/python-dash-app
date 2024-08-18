from dash import Dash

from app.callbacks.mock_list import register_mock_list_callbacks
from app.callbacks.file_list import register_file_list_callbacks

def register_all_callbacks(app: Dash)-> None:  # pylint: disable=unused-argument
    # register_mock_list_callbacks(app)
    register_file_list_callbacks(app)
