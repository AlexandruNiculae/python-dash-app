import os
import yaml


class NetworkConfig:
    host: str
    port: int

class Config:

    def __init__(self, config_yaml_path: str) -> None:
        with open(config_yaml_path, "r") as fp:
            yaml_data = yaml.safe_load(fp)
        
        self.networking = NetworkConfig(**yaml_data.get("network"))



APP_OWNER = os.environ.get("DASH_APP_OWNER", "Unknown")
CONFIG_PATH = os.environ.get("DASH_APP_CONFIG")
CONFIG = Config(CONFIG_PATH)

