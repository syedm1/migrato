import unittest
import os
import json
import pytest
from config_manager import ConfigManager
from enums.comparison_types import ComparisonType

class TestConfigManager(unittest.TestCase):

    def test_load_valid_config(self):
        config_data = {
            "old_endpoint": "http://localhost:8000/test_data/old_data.json",
            "new_endpoint": "http://localhost:8000/test_data/new_data.json",
            "comparisons": [
                {
                    "comparison_type": "exact",
                    "start_depth_old": "data",
                    "start_depth_new": "data"
                }
            ]
        }
        os.makedirs("test_data", exist_ok=True)
        with open("test_data/mock_config.json", "w") as f:
            json.dump(config_data, f)

        config_manager = ConfigManager.get_instance()
        config_manager.load_config('test_data/mock_config.json')
        loaded_config = config_manager.get_config()
        self.assertEqual(loaded_config['old_endpoint'], config_data['old_endpoint'])
        self.assertEqual(loaded_config['new_endpoint'], config_data['new_endpoint'])
        self.assertEqual(loaded_config['comparisons'][0]['comparison_type'], 
                         ComparisonType.get_enum_from_string(config_data['comparisons'][0]['comparison_type']))
        self.assertEqual(loaded_config['comparisons'][0]['start_depth_old'], config_data['comparisons'][0]['start_depth_old'])
        self.assertEqual(loaded_config['comparisons'][0]['start_depth_new'], config_data['comparisons'][0]['start_depth_new'])

        os.remove("test_data/mock_config.json")
        os.rmdir("test_data")

    def test_load_invalid_config(self):
        invalid_config_data = "invalid json"
        os.makedirs("test_data", exist_ok=True)
        with open("test_data/invalid_config.json", "w") as f:
            f.write(invalid_config_data)

        config_manager = ConfigManager.get_instance()
        with self.assertRaises(ValueError):
            config_manager.load_config('test_data/invalid_config.json')

        os.remove("test_data/invalid_config.json")
        os.rmdir("test_data")

    def test_singleton_behavior(self):
        config_manager1 = ConfigManager.get_instance()
        config_manager2 = ConfigManager.get_instance()
        self.assertIs(config_manager1, config_manager2)

if __name__ == '__main__':
    unittest.main()