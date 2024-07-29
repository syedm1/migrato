import unittest
import json
import os

from MigrateCommand import MigrateCommand
from RegressionCommand import RegressionCommand
from config_manager import ConfigManager

class TestCommands(unittest.TestCase):

    def setUp(self):
        os.makedirs("test_data", exist_ok=True)
        old_data = {"accounts": {
            "list": [{"id": 1, "name": "John Doe", "balance": 5000}, {"id": 2, "name": "Jane Doe", "balance": 7500}]}}
        new_data = {"accounts": {
            "list": [{"id": 1, "name": "John Doe", "balance": 5000}, {"id": 2, "name": "Jane Doe", "balance": 7500}]}}

        with open("test_data/old_data_1.json", "w") as f:
            json.dump(old_data, f)
        with open("test_data/new_data_1.json", "w") as f:
            json.dump(new_data, f)

        test_data = [
            {"endpoint": "http://localhost:8000/old_data_1.json", "expected": 200},
            {"endpoint": "http://localhost:8000/new_data_1.json", "expected": 200}
        ]

        with open("test_data/endpoints.csv", "w") as f:
            f.write("endpoint,expected\n")
            for item in test_data:
                f.write(f"{item['endpoint']},{item['expected']}\n")

        config = {
            "comparisons": [
                {
                    "comparison_type": "exact",
                    "start_depth_old": "",
                    "start_depth_new": ""
                }
            ]
        }

        with open("test_data/config.json", "w") as f:
            json.dump(config, f)

    def tearDown(self):
        os.remove("test_data/old_data_1.json")
        os.remove("test_data/new_data_1.json")
        os.remove("test_data/endpoints.csv")
        os.remove("test_data/config.json")

        try:
            os.rmdir("test_data")
        except OSError:
            pass

    def test_migrate_command(self):
        old_endpoint = "test_data/old_data_1.json"
        new_endpoint = "test_data/new_data_1.json"
        command = MigrateCommand(old_endpoint, new_endpoint, 'test_data/config.json')
        self.assertTrue(command.execute())

    def test_regression_test_command(self):
        config_manager = ConfigManager.get_instance()
        config_manager.load_config('test_data/config.json')
        csv_file = "test_data/endpoints.csv"
        command = RegressionCommand(csv_file)
        self.assertTrue(command.execute())

if __name__ == '__main__':
    unittest.main()