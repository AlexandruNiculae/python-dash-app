from dash import Dash

from app.callbacks.image_grid import register_callbacks as register_image_grid_callbacks


def register_all_callbacks(app: Dash)-> None:
    register_image_grid_callbacks(app)
