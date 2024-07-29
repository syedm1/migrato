import pytest
import json
import os

from MigrateCommand import MigrateCommand
from config_manager import ConfigManager

@pytest.fixture(scope="module")
def setup_data():
    os.makedirs("test_data", exist_ok=True)
    old_data = {"accounts": {
        "list": [{"id": 1, "name": "John Doe", "balance": 5000}, {"id": 2, "name": "Jane Doe", "balance": 7500}]}}
    new_data = {"accounts": {
        "list": [{"id": 1, "name": "John Doe", "balance": 5000}, {"id": 2, "name": "Jane Doe", "balance": 7500}]}}

    with open("test_data/old_data_1.json", "w") as f:
        json.dump(old_data, f)
    with open("test_data/new_data_1.json", "w") as f:
        json.dump(new_data, f)
    yield
    os.remove("test_data/old_data_1.json")
    os.remove("test_data/new_data_1.json")
    os.rmdir("test_data")

def test_exact_match(setup_data):
    config_manager = ConfigManager.get_instance()
    config_manager.load_config('config.json')
    old_endpoint = "test_data/old_data_1.json"
    new_endpoint = "test_data/new_data_1.json"
    command = MigrateCommand(old_endpoint, new_endpoint)
    assert command.execute()