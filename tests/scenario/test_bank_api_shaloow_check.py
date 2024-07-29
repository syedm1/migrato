import unittest
import os
import json
from comparison_strategies.factory import ComparisonStrategyFactory


class TestBankingAPIMigrationScenario(unittest.TestCase):

    def setUp(self):
        # Setup mock data for testing
        self.old_data = {
            "root": {
                "accounts": {
                    "oldBalances": [
                        {"accountId": "acc1", "balance": 500.0},
                        {"accountId": "acc2", "balance": 1500.0}
                    ]
                }
            }
        }
        self.new_data = {
            "accounts": {
                "newBalances": [
                    {"accountId": "acc1", "balance": 500.0},
                    {"accountId": "acc2", "balance": 1500.0},
                ],
                "newExcitingData":"hello"
            }
        }



    def test_shape_pseudo_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'pseudo',
            'start_depth_old': 'root.accounts',
            'start_depth_new': 'accounts'
        })
        result = strategy.compare(self.old_data, self.new_data)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
