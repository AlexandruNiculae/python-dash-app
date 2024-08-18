import dash_mantine_components as dmc

from app.layouts.mock_list.mock_list_item import MockListItem

# pylint: disable=too-few-public-methods

class MockList:

    def __init__(self, item_count: int) -> None:
        self.item_count = item_count

    def render(self) -> dmc.Grid:
        list_items = [
           MockListItem(i) for i in range(self.item_count)
        ]

        return dmc.Grid(children=[
                dmc.GridCol(
                    item.render()
                ) for item in list_items
            ],
            gutter="xs",
            justify="space-around",
            align="stretch",
            columns=36,
            grow=True,
        )
