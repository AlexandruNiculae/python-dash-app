import os
import dash_mantine_components as dmc

# pylint: disable=too-few-public-methods

class FileListItem:

    def __init__(self, filepath: str) -> None:
        filename = os.path.basename(filepath)
        self.filename = ".".join(filename.split('.')[:-1])
        self.filetype = filename.split('.')[-1]

        self._size_bytes = os.path.getsize(filepath)
        self.filesize = self._process_size(self._size_bytes)

    @staticmethod
    def _process_size(size: float | int) -> str:
        size_category = "B"
        final_size = size
        if final_size > 1024:
            final_size /= 1024
            size_category = "KB"

        if final_size > 1024:
            final_size /= 1024
            size_category = "MB"

        if final_size > 1024:
            final_size /= 1024
            size_category = "GB"

        return f"{round(final_size, 2)} {size_category}"


    def render(self) -> dmc.GridCol:
        return dmc.GridCol(
            children=[
                dmc.Card(
                    children=[
                        dmc.CardSection(
                            dmc.Center(dmc.Text(self.filename)),
                        ),
                        dmc.Group(
                            [
                                dmc.Text(f"File type: {self.filetype}"),
                                dmc.Text(f"Size: {self.filesize}"),
                            ],
                            justify="center",
                            mt="md",
                            mb="xs",
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    w=500,
                )
            ],
        )
