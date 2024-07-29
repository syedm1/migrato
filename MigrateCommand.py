import utils
from comparison_strategies.factory import ComparisonStrategyFactory
from config_manager import ConfigManager
import logging

class MigrateCommand:
    def __init__(self, old_endpoint, new_endpoint):
        self.old_endpoint = old_endpoint
        self.new_endpoint = new_endpoint
        self.logger = logging.getLogger(__name__)

    def execute(self):
        try:
            config = ConfigManager.get_instance().get_config()
            old_data, old_status = utils.fetch_data(self.old_endpoint)
            new_data, new_status = utils.fetch_data(self.new_endpoint)

            if old_status != 200 or new_status != 200:
                self.logger.error(
                    f"Failed to fetch data: Old endpoint status {old_status}, New endpoint status {new_status}")
                return False



            self.logger.debug("Old data fetched: %s", old_data)
            self.logger.debug("New data fetched: %s", new_data)

            comparisons = config['comparisons']
            for comparison in comparisons:
                strategy = ComparisonStrategyFactory.get_comparison_strategy(comparison)
                result = strategy.compare(old_data, new_data)

                self.logger.debug("Comparison result for %s: %s", comparison['comparison_type'], result)

                if not result:
                    self.logger.error("%s comparison failed", comparison['comparison_type'])
                    return False

            self.logger.info("All comparisons succeeded")
            return True

        except Exception as e:
            self.logger.exception("Exception occurred during execution")
            return False