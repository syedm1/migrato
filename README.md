

# Migrato

Migrato is a powerful tool designed to test API endpoint migrations. It compares data from an old endpoint with data from a new endpoint based on various comparison types, including exact matches, shape matches, custom mappings, specific matches, and pseudo matches. Migrato can handle complex nested structures and supports ignoring specific keys during comparison.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Supported Comparison Keys](#supported-comparison-keys)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Compare data from old and new endpoints
- Support for various comparison types: exact, shape, custom, specific, pseudo
- Handle nested structures
- Ignore specific keys during comparison
- Provide detailed match and mismatch information
- **New**: Regression testing for multiple API calls

## Installation

Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/yourusername/migrato.git
cd migrato
```

Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Start the mock server:

```sh
python server.py
```

Run the migrato tool with a configuration file:

```sh
python migrato.py path/to/config.json
```

For regression testing with multiple API calls using a CSV file:

```sh
python migrato.py path/to/config.json --testRegression --csv_file path/to/endpoints.csv
```

## Configuration

The configuration file is a JSON file that specifies the endpoints and comparison details. Here is an example configuration file:

```json
{
    "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s/userId/{user_id}",
    "new_endpoint": "http://localhost:8000/test_data/latestEndpoint/customer/{user_id}",
    "comparisons": [
        {
            "comparison_type": "exact",
            "start_depth_old": "root.level1.level2",
            "start_depth_new": "root.levelA.levelB"
        },
        {
            "comparison_type": "custom",
            "custom_mapping": {
                "oldKey1": "newKey1",
                "oldKey2": "newKey2"
            },
            "start_depth_old": "root.oldPath",
            "start_depth_new": "root.newPath",
            "ignore_keys": ["timestamp"]
        },
        {
            "comparison_type": "orderingCheck",
            "start_depth_old": "transactions",
            "start_depth_new": "transactions"
        }
    ]
}
```

### Supported Comparison Keys

- `exact`: Compares if the data is exactly the same.
- `shape`: Compares if the data structure and length are the same.
- `custom`: Maps old keys to new keys for comparison.
- `specific`: Compares specific nested structures.
- `pseudo`: Provides detailed

 information on matched and unmatched keys.
- `orderingCheck`: Checks if the order of elements is maintained.

## Examples

### Example 1: Exact Match

Comparing customer details from the 2000s to the latest system:

**Configuration:**

```json
{
    "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s/customerDetails.json",
    "new_endpoint": "http://localhost:8000/test_data/latestEndpoint/customerDetails.json",
    "comparisons": [
        {
            "comparison_type": "exact",
            "start_depth_old": "customerInfo",
            "start_depth_new": "customerData"
        }
    ]
}
```

### Example 2: Custom Mapping

Comparing transaction data with different key names:

**Configuration:**

```json
{
    "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s/transactions.json",
    "new_endpoint": "http://localhost:8000/test_data/latestEndpoint/transactions.json",
    "comparisons": [
        {
            "comparison_type": "custom",
            "custom_mapping": {
                "oldTransactionID": "newTransactionID",
                "oldAmount": "newAmount"
            },
            "start_depth_old": "transactions.oldFormat",
            "start_depth_new": "transactions.newFormat",
            "ignore_keys": ["timestamp"]
        }
    ]
}
```

### Example 3: Pseudo Match

Providing detailed information on matched and unmatched keys for bank account balances:

**Configuration:**

```json
{
    "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s/accountBalances.json",
    "new_endpoint": "http://localhost:8000/test_data/latestEndpoint/accountBalances.json",
    "comparisons": [
        {
            "comparison_type": "pseudo",
            "start_depth_old": "accounts.oldBalances",
            "start_depth_new": "accounts.newBalances"
        }
    ]
}
```

### Example 4: Ordering Check

Ensuring the order of transactions is maintained:

**Configuration:**

```json
{
    "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s/transactions.json",
    "new_endpoint": "http://localhost:8000/test_data/latestEndpoint/transactions.json",
    "comparisons": [
        {
            "comparison_type": "orderingCheck",
            "start_depth_old": "transactions.oldOrder",
            "start_depth_new": "transactions.newOrder"
        }
    ]
}
```

### Example 5: Regression Testing

Regression testing across multiple user endpoints:

**CSV File (endpoints.csv):**

```
old_endpoint,new_endpoint
http://localhost:8000/test_data/endpointFrom2000s/userId/2,http://localhost:8000/test_data/latestEndpoint/customer/2
http://localhost:8000/test_data/endpointFrom2000s/userId/3,http://localhost:8000/test_data/latestEndpoint/customer/3
...
http://localhost:8000/test_data/endpointFrom2000s/userId/100,http://localhost:8000/test_data/latestEndpoint/customer/100
```

**Configuration:**

```json
{
    "comparisons": [
        {
            "comparison_type": "exact",
            "start_depth_old": "userInfo",
            "start_depth_new": "customerData"
        },
        {
            "comparison_type": "custom",
            "custom_mapping": {
                "oldTransactionID": "newTransactionID",
                "oldAmount": "newAmount"
            },
            "start_depth_old": "transactions.oldFormat",
            "start_depth_new": "transactions.newFormat",
            "ignore_keys": ["timestamp"]
        },
        {
            "comparison_type": "orderingCheck",
            "start_depth_old": "transactions",
            "start_depth_new": "transactions"
        }
    ]
}
```

Run the migrato tool with the regression testing flag and CSV file:

```sh
python migrato.py path/to/config.json --testRegression --csv_file path/to/endpoints.csv
```

## Contributing

We welcome contributions from the community! Please read our [contributing guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This documentation provides a comprehensive overview of Migrato, its features, and how to use it with various examples. Feel free to customize and expand it as needed for your project.
