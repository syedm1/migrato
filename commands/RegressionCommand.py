import logging
import csv
from config_manager import ConfigManager
import MigrateCommand
from commands.command import Command


class RegressionCommand(Command):
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
