import os


from src.config import APP_OWNER


def test_app_owner_is_set()-> None:
    assert APP_OWNER != "Nobody", "Variable DASH_APP_OWNER is not set"


def test_app_config_is_set()-> None:
    confpath = os.environ.get("DASH_APP_CONFIG")
    assert confpath is not None, "Variable DASH_APP_CONFIG is not set"
