import unittest
from comparison_strategies.factory import ComparisonStrategyFactory
from utils import get_nested_value, remove_ignored_keys

class TestComparisons(unittest.TestCase):

    def test_exact_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'exact',
            'start_depth_old': '',
            'start_depth_new': ''
        })
        old_data = {"key1": "value1", "key2": "value2"}
        new_data = {"key1": "value1", "key2": "value2"}
        result = strategy.compare(old_data, new_data)
        self.assertTrue(result)

    def test_exact_comparison_failure(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'exact',
            'start_depth_old': '',
            'start_depth_new': ''
        })
        old_data = {"key1": "value1", "key2": "value2"}
        new_data = {"key1": "value1", "key2": "different_value"}
        result = strategy.compare(old_data, new_data)
        self.assertFalse(result)

    def test_shape_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'shape',
            'start_depth_old': '',
            'start_depth_new': ''
        })
        old_data = {"key1": "value1", "key2": "value2"}
        new_data = {"key1": "value1", "key2": "value2"}
        result = strategy.compare(old_data, new_data)
        self.assertTrue(result)

    def test_shape_comparison_failure(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'shape',
            'start_depth_old': '',
            'start_depth_new': ''
        })
        old_data = {"key1": "value1", "key2": "value2"}
        new_data = {"key1": "value1", "key2": "different_value", "key3": "value3"}
        result = strategy.compare(old_data, new_data)
        self.assertFalse(result)

    def test_custom_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'custom',
            'custom_mapping': {'key1': 'keyA', 'key2': 'keyB'}
        })
        old_data = {"key1": "value1", "key2": "value2"}
        new_data = {"keyA": "value1", "keyB": "value2"}
        result = strategy.compare(old_data, new_data)
        self.assertTrue(result)

    def test_specific_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'specific',
            'specific_match': {'old': 'key1', 'new': 'keyA'}
        })
        old_data = {"key1": "value1"}
        new_data = {"keyA": "value1"}
        result = strategy.compare(old_data, new_data)
        self.assertTrue(result)

    def test_specific_comparison_failure(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'specific',
            'specific_match': {'old': 'key1', 'new': 'keyA'}
        })
        old_data = {"key1": "value1"}
        new_data = {"keyA": "different_value"}
        result = strategy.compare(old_data, new_data)
        self.assertFalse(result)

    def test_pseudo_comparison(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'pseudo',
            'start_depth_old': '',
            'start_depth_new': ''
        })
        old_data = {"key1": "value1", "key2": "value2"}
        new_data = {"key1": "value1", "key2": "value2"}
        matched_keys, failed_keys = strategy.compare(old_data, new_data)
        self.assertEqual(matched_keys, old_data)
        self.assertEqual(failed_keys, {})

    def test_pseudo_comparison_failure(self):
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'pseudo',
            'start_depth_old': '',
            'start_depth_new': ''
        })
        old_data = {"key1": "value1", "key2": "value2"}
        new_data = {"key1": "value1", "key2": "different_value"}
        matched_keys, failed_keys = strategy.compare(old_data, new_data)
        self.assertEqual(matched_keys, {"key1": "value1"})
        self.assertEqual(failed_keys, {"key2": {"old_value": "value2", "new_value": "different_value"}})

    def test_ignore_keys(self):
        old_data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        new_data = {"key1": "value1", "key2": "different_value", "key3": "value3"}
        ignore_keys = ["key2"]
        old_segment = remove_ignored_keys(old_data, ignore_keys)
        new_segment = remove_ignored_keys(new_data, ignore_keys)
        strategy = ComparisonStrategyFactory.get_comparison_strategy({
            'comparison_type': 'exact',
            'start_depth_old': '',
            'start_depth_new': ''
        })
        result = strategy.compare(old_segment, new_segment)
        self.assertTrue(result)

    def test_get_nested_value(self):
        data = {"level1": {"level2": {"key": "value"}}}
        value = get_nested_value(data, "level1.level2.key")
        self.assertEqual(value, "value")


if __name__ == '__main__':
    unittest.main()