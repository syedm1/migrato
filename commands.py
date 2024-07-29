import logging
import csv
from config_manager import ConfigManager
from Comparisions.comparisons import ComparisonStrategyFactory, get_nested_value
from utils import fetch_data, remove_ignored_keys

class Command:
    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class MigrateCommand(Command):
    def __init__(self, old_endpoint=None, new_endpoint=None):
        self.old_endpoint = old_endpoint
        self.new_endpoint = new_endpoint

    def execute(self):
        config_manager = ConfigManager.get_instance()
        config = config_manager.get_config()

        if self.old_endpoint is None:
            self.old_endpoint = config['old_endpoint']
        if self.new_endpoint is None:
            self.new_endpoint = config['new_endpoint']

        old_data = fetch_data(self.old_endpoint)
        new_data = fetch_data(self.new_endpoint)

        for comparison in config['comparisons']:
            strategy = ComparisonStrategyFactory.get_comparison_strategy(comparison)
            start_depth_old = comparison.get('start_depth_old', '')
            start_depth_new = comparison.get('start_depth_new', '')
            ignore_keys = comparison.get('ignore_keys', [])

            old_segment = get_nested_value(old_data, start_depth_old) if start_depth_old else old_data
            new_segment = get_nested_value(new_data, start_depth_new) if start_depth_new else new_data

            old_segment = remove_ignored_keys(old_segment, ignore_keys)
            new_segment = remove_ignored_keys(new_segment, ignore_keys)

            result = strategy.compare(old_segment, new_segment)

            if comparison.get('comparison_type') == 'pseudo':
                matched_keys, failed_keys = result
                logging.info(f"Pseudo comparison matched keys: {matched_keys}")
                logging.info(f"Pseudo comparison failed keys: {failed_keys}")
                result = not failed_keys

            if not result:
                logging.warning(f"Comparison failed for type: {comparison['comparison_type']}")
                return False

        logging.info("Migration successful. Data matches as per the comparison type.")
        return True

class RegressionTestCommand(Command):
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def execute(self):
        config_manager = ConfigManager.get_instance()
        config = config_manager.get_config()

        endpoints = []
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                endpoints.append((row['old_endpoint'], row['new_endpoint']))

        for old_endpoint, new_endpoint in endpoints:
            logging.info(f"Testing old endpoint: {old_endpoint} with new endpoint: {new_endpoint}")
            if not MigrateCommand(old_endpoint, new_endpoint).execute():
                logging.warning(f"Migration failed for old endpoint: {old_endpoint} with new endpoint: {new_endpoint}")
                break
