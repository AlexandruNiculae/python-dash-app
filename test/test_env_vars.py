import os


from src.config import APP_OWNER


def test_app_owner_is_set()-> None:
    assert APP_OWNER != "Nobody", "Variable DASH_APP_OWNER is not set"


def test_host_is_set()-> None:
    host = os.environ.get("HOST", "127.0.0.1")
    assert host != "127.0.0.1", "Variable HOST is not set"