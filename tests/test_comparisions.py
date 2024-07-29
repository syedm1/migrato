# tests/test_comparisons.py

import unittest
from comparison_strategies.factory import ComparisonStrategyFactory
from utils import get_nested_value, remove_ignored_keys


def test_exact_comparison():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'exact'})
    old_data = {"key1": "value1", "key2": "value2"}
    new_data = {"key1": "value1", "key2": "value2"}
    result = strategy.compare(old_data, new_data)
    assert result


def test_exact_comparison_failure():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'exact'})
    old_data = {"key1": "value1", "key2": "value2"}
    new_data = {"key1": "value1", "key2": "different_value"}
    result = strategy.compare(old_data, new_data)
    assert not result


def test_shape_comparison():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'shape'})
    old_data = {"key1": "value1", "key2": "value2"}
    new_data = {"key1": "value1", "key2": "value2"}
    result = strategy.compare(old_data, new_data)
    assert result


def test_shape_comparison_failure():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'shape'})
    old_data = {"key1": "value1", "key2": "value2"}
    new_data = {"key1": "value1", "key2": "different_value", "key3": "value3"}
    result = strategy.compare(old_data, new_data)
    assert not result


def test_custom_comparison():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({
        'comparison_type': 'custom',
        'custom_mapping': {'key1': 'keyA', 'key2': 'keyB'}
    })
    old_data = {"key1": "value1", "key2": "value2"}
    new_data = {"keyA": "value1", "keyB": "value2"}
    result = strategy.compare(old_data, new_data)
    assert result


def test_specific_comparison():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({
        'comparison_type': 'specific',
        'specific_match': {'old': 'key1', 'new': 'keyA'}
    })
    old_data = {"key1": "value1"}
    new_data = {"keyA": "value1"}
    result = strategy.compare(old_data, new_data)
    assert result


def test_specific_comparison_failure():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({
        'comparison_type': 'specific',
        'specific_match': {'old': 'key1', 'new': 'keyA'}
    })
    old_data = {"key1": "value1"}
    new_data = {"keyA": "different_value"}
    result = strategy.compare(old_data, new_data)
    assert not result


def test_pseudo_comparison():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'pseudo'})
    old_data = {"key1": "value1", "key2": "value2"}
    new_data = {"key1": "value1", "key2": "value2"}
    matched_keys, failed_keys = strategy.compare(old_data, new_data)
    assert matched_keys == old_data
    assert failed_keys == {}


def test_pseudo_comparison_failure():
    strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'pseudo'})
    old_data = {"key1": "value1", "key2": "value2"}
    new_data = {"key1": "value1", "key2": "different_value"}
    matched_keys, failed_keys = strategy.compare(old_data, new_data)
    assert matched_keys == {"key1": "value1"}
    assert failed_keys == {"key2": {"old_value": "value2", "new_value": "different_value"}}


def test_ignore_keys():
    old_data = {"key1": "value1", "key2": "value2", "key3": "value3"}
    new_data = {"key1": "value1", "key2": "different_value", "key3": "value3"}
    ignore_keys = ["key2"]
    old_segment = remove_ignored_keys(old_data, ignore_keys)
    new_segment = remove_ignored_keys(new_data, ignore_keys)
    strategy = ComparisonStrategyFactory.get_comparison_strategy({'comparison_type': 'exact'})
    result = strategy.compare(old_segment, new_segment)
    assert result


def test_get_nested_value():
    data = {"level1": {"level2": {"key": "value"}}}
    value = get_nested_value(data, "level1.level2.key")
    assert value == "value"


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.FunctionTestCase(test_exact_comparison))
    test_suite.addTest(unittest.FunctionTestCase(test_exact_comparison_failure))
    test_suite.addTest(unittest.FunctionTestCase(test_shape_comparison))
    test_suite.addTest(unittest.FunctionTestCase(test_shape_comparison_failure))
    test_suite.addTest(unittest.FunctionTestCase(test_custom_comparison))
    test_suite.addTest(unittest.FunctionTestCase(test_specific_comparison))
    test_suite.addTest(unittest.FunctionTestCase(test_specific_comparison_failure))
    test_suite.addTest(unittest.FunctionTestCase(test_pseudo_comparison))
    test_suite.addTest(unittest.FunctionTestCase(test_pseudo_comparison_failure))
    test_suite.addTest(unittest.FunctionTestCase(test_ignore_keys))
    test_suite.addTest(unittest.FunctionTestCase(test_get_nested_value))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())