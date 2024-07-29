import unittest
from utils import get_nested_value, remove_ignored_keys

class TestUtils(unittest.TestCase):

    def test_get_nested_value(self):
        data = {"level1": {"level2": {"key": "value"}}}
        value = get_nested_value(data, "level1.level2.key")
        self.assertEqual(value, "value")

    def test_get_nested_value_invalid_key(self):
        data = {"level1": {"level2": {"key": "value"}}}
        with self.assertRaises(KeyError):
            get_nested_value(data, "level1.level2.invalid_key")

    def test_remove_ignored_keys(self):
        data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        ignore_keys = ["key2"]
        result = remove_ignored_keys(data, ignore_keys)
        expected_result = {"key1": "value1", "key3": "value3"}
        self.assertEqual(result, expected_result)

    def test_remove_ignored_keys_no_ignored(self):
        data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        ignore_keys = []
        result = remove_ignored_keys(data, ignore_keys)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()