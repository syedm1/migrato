import pytest
import subprocess
import time
import json
import os
import requests
import logging
from migrato import ConfigManager
from commands import MigrateCommand


@pytest.fixture(scope="module")
def start_server():
    # Start the mock server
    server = subprocess.Popen(["python", "-m", "http.server", "8000"])
    time.sleep(1)  # Give the server a moment to start
    yield
    server.terminate()


@pytest.fixture(scope="module")
def create_test_data():
    os.makedirs("test_data", exist_ok=True)

    # Create minimal mock data for testing
    old_data = {"data": {"value": "old"}}
    new_data = {"data": {"value": "new"}}

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

    with open("test_data/mock_config.json", "w") as f:
        json.dump(config_data, f)

    with open("test_data/old_data.json", "w") as f:
        json.dump(old_data, f)
    with open("test_data/new_data.json", "w") as f:
        json.dump(new_data, f)

    yield

    # Cleanup
    os.remove("test_data/old_data.json")
    os.remove("test_data/mock_config.json")
    os.remove("test_data/new_data.json")
    os.rmdir("test_data")


def test_migrate_command(start_server, create_test_data):
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    config_manager = ConfigManager.get_instance()
    config_manager.load_config('test_data/mock_config.json')

    # Log the loaded config for debugging
    logger.debug("Loaded config: %s", config_manager.get_config())

    # Fetch and log the old data for debugging
    old_response = requests.get(config_manager.get_config()['old_endpoint'])
    logger.debug("Old data response: %s", old_response.json())

    # Fetch and log the new data for debugging
    new_response = requests.get(config_manager.get_config()['new_endpoint'])
    logger.debug("New data response: %s", new_response.json())

    command = MigrateCommand()

    try:
        result = command.execute()
        assert result
    except Exception as e:
        logger.exception("Command execution failed")
        pytest.fail(f"Command execution failed: {e}")


if __name__ == "__main__":
    pytest.main()
