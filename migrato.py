import requests
import logging
from config_manager import ConfigManager
from enums import comparison_types as ComparisonType


class MigrateCommand:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def execute(self):
        try:
            config = ConfigManager.get_instance().get_config()
            old_response = requests.get(config['old_endpoint'])
            new_response = requests.get(config['new_endpoint'])

            if old_response.status_code != 200 or new_response.status_code != 200:
                self.logger.error(
                    f"Failed to fetch data: Old endpoint status {old_response.status_code}, New endpoint status {new_response.status_code}")
                return False

            old_data = old_response.json()
            new_data = new_response.json()

            # Log data for debugging
            self.logger.debug("Old data fetched: %s", old_data)
            self.logger.debug("New data fetched: %s", new_data)

            comparisons = config['comparisons']
            for comparison in comparisons:
                if comparison['comparison_type'] == ComparisonType.EXACT:
                    if not self.compare_exact(old_data, new_data, comparison['start_depth_old'],
                                              comparison['start_depth_new']):
                        self.logger.error("Exact comparison failed")
                        return False
            self.logger.info("All comparisons succeeded")
            return True

        except Exception as e:
            self.logger.exception("Exception occurred during execution")
            return False

    def compare_exact(self, old_data, new_data, start_depth_old, start_depth_new):
        # Navigate to the start depth
        old_value = self.get_nested_value(old_data, start_depth_old.split('.'))
        new_value = self.get_nested_value(new_data, start_depth_new.split('.'))

        # Log values for debugging
        self.logger.debug("Comparing exact values: Old value %s, New value %s", old_value, new_value)

        return old_value == new_value

    def get_nested_value(self, data, keys):
        for key in keys:
            data = data.get(key, {})
        return data
