from typing import Any

from dash import html
import dash_mantine_components as dmc

# pylint: disable=too-few-public-methods

style = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "textAlign": "center",
}

class MockListItem:

    def __init__(self, item_idx: int, **kwargs: dict[Any, Any]) -> None:
        self.item_idx = item_idx
        self.kwargs = kwargs


    def render(self) -> dmc.GridCol:
        return dmc.GridCol(
            children=[
                html.Div(self.item_idx, style=style)
            ],
        )
