import os
import dash_mantine_components as dmc

from app.layouts.file_list_item import FileListItem

# pylint: disable=too-few-public-methods

class FileList:

    def __init__(self, dirpath: str) -> None:
        self.dirpath = dirpath
        self.ignored_extensions = [
            "ini",
            "bin",
            "tmp",
        ]

    def render(self) -> dmc.Grid:
        list_items = [
            FileListItem(
                filepath=os.path.join(self.dirpath, filename)
            ) for filename in os.listdir(self.dirpath)
        ]

        return dmc.Grid(gutter="xs", children=[
            dmc.GridCol(
                item.render()
            ) for item in list_items if item.filetype not in self.ignored_extensions
        ])
