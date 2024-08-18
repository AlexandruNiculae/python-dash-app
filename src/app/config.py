import os
import yaml

from dataclasses import dataclass

@dataclass
class NetworkConfig:
    host: str
    port: int


@dataclass
class DataConfig:
    path: str

class AppConfig:  # pylint: disable=too-few-public-methods

    def __init__(self, config_yaml_path: str) -> None:
        with open(config_yaml_path, "r") as fp:
            yaml_data = yaml.safe_load(fp)

        self.networking = NetworkConfig(**yaml_data.get("network"))
        self.data = DataConfig(**yaml_data.get("data"))



APP_OWNER = os.environ.get("DASH_APP_OWNER", "Unknown")
CONFIG_PATH = os.environ.get("DASH_APP_CONFIG", "config.yaml")
CONFIG = AppConfig(CONFIG_PATH)
