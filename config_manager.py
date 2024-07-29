import json
import os
from enums.comparison_types import ComparisonType

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
        for comparison in self.config['comparisons']:
            comparison['comparison_type'] = ComparisonType.get_enum_from_string(comparison['comparison_type'])

    def get_config(self):
        return self.config

    def _validate_config(self, config):
        required_keys = ["old_endpoint", "new_endpoint", "comparisons"]
        for key in required_keys:
            if key not in config:
                print(f"Missing key: {key}")
                return False

        if not isinstance(config["comparisons"], list):
            print("Comparisons is not a list")
            return False

        for comparison in config["comparisons"]:
            if "comparison_type" not in comparison or "start_depth_old" not in comparison or "start_depth_new" not in comparison:
                print(f"Missing keys in comparison: {comparison}")
                return False

            if not ComparisonType.is_valid_enum(comparison["comparison_type"].lower()):
                print(f"Invalid comparison type: {comparison['comparison_type']}")
                return False

        return True