from typing import Any
from dash import Dash, Input, Output

from app.layouts.image_grid import ImageGridLayout


def register_callbacks(app: Dash)-> None:
    @app.callback(
        Output('main-canvas', 'children', allow_duplicate=True),
        Input('main-one-time-interval', 'n_intervals'),
        prevent_initial_call=True
    )
    def generate_grid_layout(_: Any) -> Any:
        return ImageGridLayout().render()