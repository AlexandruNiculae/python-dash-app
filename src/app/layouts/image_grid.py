from dash import html
import dash_mantine_components as dmc

from storage import get_storage


class ImageGridLayout(dmc.Stack):

    def __init__(self) -> None:
        self.image_storage = get_storage()

    def render(self) -> dmc.Grid:
        img_objects = [
            html.Img(
                src=self.image_storage.get_image_data(img_url),
                style={"height": 200}
            ) for img_url in self.image_storage.get_image_urls()
        ]


        return dmc.Grid(gutter="xs", children=[
            dmc.GridCol(
                dmc.Center(
                    style={"height": 200, "width": "100%"},
                    children=[
                        img
                    ],
                ),
                span=2
            ) for img in img_objects
        ])
