import configparser
import os


class ConfigLoader:
    def __init__(self, config_file: str):
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Config file not found: {config_file}")

        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, key: str, default=None):
        """Get a value from [DEFAULT] section."""
        return self.config["DEFAULT"].get(key, default)
