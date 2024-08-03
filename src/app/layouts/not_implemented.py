import dash_mantine_components as dmc

# pylint: disable=too-few-public-methods

class NotImplementedComponent:

    def __init__(self) -> None:
        pass

    def render(self) -> dmc.Stack:
        return dmc.Stack(
            [
            dmc.Title("Component not implemented"),
            dmc.Text("This component is not implemented yet."),
            dmc.Text("Make sure you have the latest verison of the app.")
            ]
        )
