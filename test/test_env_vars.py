import os


from src.config import APP_OWNER


def test_app_owner_is_set()-> None:
    assert APP_OWNER != "Nobody"