import unittest


from comparison_strategies.factory import ComparisonStrategyFactory



class TestBankingAPIMigration(unittest.TestCase):

    def setUp(self):
        # Setup mock data for testing
        self.old_data = {
            "account": {
                "id": "12345",
                "balance": 1000.0,
                "transactions": [
                    {"id": "txn1", "amount": -100.0},
                    {"id": "txn2", "amount": 200.0}
                ]
            }
        }
        self.new_data = {
            "account": {
                "id": "12345",
                "balance": 1100.0,
                "transactions": [
                    {"id": "txn1", "amount": -100.0},
                    {"id": "txn2", "amount": 200.0},
                    {"id": "txn3", "amount": 100.0}
                ]
            }
        }

        self.old_data_with_customer_id = {
            "customer": {
                "id": "67890",
                "account": {
                    "id": "12345",
                    "balance": 1000.0,
                    "transactions": [
                        {"id": "txn1", "amount": -100.0},
                        {"id": "txn2", "amount": 200.0}
                    ]
                }
            }
        }

        self.new_data_with_customer_id_as_user_id = {
            "user": {
                "id": "67890",
                "account": {
                    "id": "12345",
                    "balance": 1000.0,
                    "transactions": [
                        {"id": "txn1", "amount": -100.0},
                        {"id": "txn2", "amount": 200.0}
                    ]
                }
            }
        }

    def test_exact_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'exact'})
        result = strategy.compare(self.old_data, self.new_data)
        self.assertFalse(result)

    def test_shape_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'shape'})
        result = strategy.compare(self.old_data, self.new_data)
        self.assertTrue(result)


    def test_custom_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'custom',
            'custom_mapping': {'customer': 'user'}
        })
        result = strategy.compare(self.old_data_with_customer_id, self.new_data_with_customer_id_as_user_id)
        self.assertTrue(result)

    def test_specific_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'specific',
            'specific_match': {'old': 'customer', 'new': 'user'}
        })
        result = strategy.compare(self.old_data_with_customer_id, self.new_data_with_customer_id_as_user_id)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()