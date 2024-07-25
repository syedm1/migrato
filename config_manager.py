import json
import os
from enums import comparison_types as ComparisonType


class ConfigManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ConfigManager._instance is None:
            ConfigManager()
        return ConfigManager._instance

    def __init__(self):
        if ConfigManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ConfigManager._instance = self
            self.config = None

    def load_config(self, config_file):
        if not os.path.isfile(config_file):
            raise ValueError(f"Config file does not exist: {config_file}")

        with open(config_file, 'r') as file:
            try:
                self.config = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Config file is not a valid JSON: {e}")

        if not self._validate_config(self.config):
            raise ValueError("Config file format is invalid")

        # Convert comparison types to enums
        self.config['comparisons'] = [
            {
                'comparison_type': ComparisonType[comp['comparison_type'].upper()],
                'start_depth_old': comp['start_depth_old'],
                'start_depth_new': comp['start_depth_new']
            }
            for comp in self.config['comparisons']
        ]

    def get_config(self):
        return self.config

    def _validate_config(self, config):
        required_keys = ["old_endpoint", "new_endpoint", "comparisons"]
        for key in required_keys:
            if key not in config:
                return False

        if not isinstance(config["comparisons"], list):
            return False

        for comparison in config["comparisons"]:
            if "comparison_type" not in comparison or "start_depth_old" not in comparison or "start_depth_new" not in comparison:
                return False

            try:
                ComparisonType(comparison["comparison_type"].upper())
            except KeyError:
                return False

        return True

