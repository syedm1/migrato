import pytest
import subprocess
import time
import json
import os
from config_manager import ConfigManager
from commands import MigrateCommand


# Test Scenario 1: Exact match for account balances
# Description: This test checks if the account balances match exactly between the old and new endpoints.
@pytest.fixture(scope="module")
def start_server():
    server = subprocess.Popen(["python", "-m", "http.server", "8000"])
    time.sleep(1)
    yield
    server.terminate()


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


def test_exact_match(start_server, setup_data):
    config_manager = ConfigManager.get_instance()
    config_manager.load_config('config.json')
    command = MigrateCommand()
    assert command.execute()
