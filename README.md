Sure! Below is a detailed markdown documentation for the open-source project `migrato`. This documentation follows a common open-source project format, explains the use of the tool, how the template works, and provides examples from the banking domain.

---

# Migrato

**Migrato** is a powerful tool designed to test API endpoint migrations. It compares data from old and new endpoints, supports various comparison types, and offers flexible configuration options. Whether you're dealing with JSON data structures from different eras or migrating endpoints for a major financial institution, Migrato has you covered.

## Features

- **Exact Match**: Compare JSON structures for an exact match.
- **Shape Match**: Compare the shape of JSON structures.
- **Custom Mapping**: Map keys from the old endpoint to new keys.
- **Specific Match**: Compare specific nested values.
- **Pseudo Match**: Show keys that matched and keys that failed.
- **Ignore Keys**: Ignore specific keys during comparison.
- **Ordering Check**: Ensure that lists maintain the same order.

## Installation

To install Migrato, clone the repository and install the dependencies:

```sh
git clone https://github.com/yourusername/migrato.git
cd migrato
pip install -r requirements.txt
```

## Usage

To use Migrato, create a configuration file that defines the old and new endpoints, the type of comparison, and any specific keys or mappings. Then, run the `migrato.py` script with the configuration file.

```sh
python migrato.py config.json
```

## Configuration File

The configuration file defines how the old and new endpoints should be compared. Below is an example configuration file:

```json
{
    "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s.json",
    "new_endpoint": "http://localhost:8000/test_data/latestEndpoint.json",
    "comparisons": [
        {
            "comparison_type": "exact",
            "start_depth_old": "transactions",
            "start_depth_new": "transactions"
        },
        {
            "comparison_type": "shape",
            "start_depth_old": "account.details",
            "start_depth_new": "profile.details"
        },
        {
            "comparison_type": "custom",
            "custom_mapping": {
                "oldName": "newName",
                "oldBalance": "currentBalance"
            },
            "start_depth_old": "account.info",
            "start_depth_new": "profile.info",
            "ignore_keys": ["timestamp"]
        },
        {
            "comparison_type": "specific",
            "specific_match": {
                "old": "account.transactions.oldFormat",
                "new": "profile.transactions.newFormat"
            }
        },
        {
            "comparison_type": "pseudo",
            "start_depth_old": "transactions",
            "start_depth_new": "transactions"
        },
        {
            "comparison_type": "exact",
            "start_depth_old": "transactions",
            "start_depth_new": "transactions",
            "orderingCheck": true
        }
    ]
}
```

## Examples

### Example 1: Exact Match

**Scenario**: Comparing transaction lists from an ancient banking system to a modern system.

- **Old Endpoint (from the 2000s)**:
    ```json
    {
        "transactions": [
            { "id": 1, "amount": 100, "timestamp": "2001-01-01T00:00:00Z" },
            { "id": 2, "amount": 200, "timestamp": "2001-01-02T00:00:00Z" }
        ]
    }
    ```

- **New Endpoint (latest)**:
    ```json
    {
        "transactions": [
            { "id": 1, "amount": 100, "timestamp": "2023-01-01T00:00:00Z" },
            { "id": 2, "amount": 200, "timestamp": "2023-01-02T00:00:00Z" }
        ]
    }
    ```

- **Configuration**:
    ```json
    {
        "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s.json",
        "new_endpoint": "http://localhost:8000/test_data/latestEndpoint.json",
        "comparisons": [
            {
                "comparison_type": "exact",
                "start_depth_old": "transactions",
                "start_depth_new": "transactions"
            }
        ]
    }
    ```

### Example 2: Custom Mapping

**Scenario**: Mapping old account details to new profile format.

- **Old Endpoint (from the 2000s)**:
    ```json
    {
        "account": {
            "info": {
                "oldName": "John Doe",
                "oldBalance": 1000,
                "timestamp": "2001-01-01T00:00:00Z"
            }
        }
    }
    ```

- **New Endpoint (latest)**:
    ```json
    {
        "profile": {
            "info": {
                "newName": "John Doe",
                "currentBalance": 1000,
                "timestamp": "2023-01-01T00:00:00Z"
            }
        }
    }
    ```

- **Configuration**:
    ```json
    {
        "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s.json",
        "new_endpoint": "http://localhost:8000/test_data/latestEndpoint.json",
        "comparisons": [
            {
                "comparison_type": "custom",
                "custom_mapping": {
                    "oldName": "newName",
                    "oldBalance": "currentBalance"
                },
                "start_depth_old": "account.info",
                "start_depth_new": "profile.info",
                "ignore_keys": ["timestamp"]
            }
        ]
    }
    ```

### Example 3: Ordering Check

**Scenario**: Ensuring the order of transactions remains the same.

- **Old Endpoint (from the 2000s)**:
    ```json
    {
        "transactions": [
            { "id": 1, "amount": 100, "timestamp": "2001-01-01T00:00:00Z" },
            { "id": 2, "amount": 200, "timestamp": "2001-01-02T00:00:00Z" }
        ]
    }
    ```

- **New Endpoint (latest)**:
    ```json
    {
        "transactions": [
            { "id": 2, "amount": 200, "timestamp": "2023-01-02T00:00:00Z" },
            { "id": 1, "amount": 100, "timestamp": "2023-01-01T00:00:00Z" }
        ]
    }
    ```

- **Configuration**:
    ```json
    {
        "old_endpoint": "http://localhost:8000/test_data/endpointFrom2000s.json",
        "new_endpoint": "http://localhost:8000/test_data/latestEndpoint.json",
        "comparisons": [
            {
                "comparison_type": "exact",
                "start_depth_old": "transactions",
                "start_depth_new": "transactions",
                "orderingCheck": true
            }
        ]
    }
    ```

## Running Tests

To run the tests, start the mock server and execute the test suite using `pytest`.

```sh
python server.py &
pytest test_migrator.py
```

## Contributing

We welcome contributions from the community! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This markdown file provides a comprehensive guide to using the Migrato tool, complete with installation instructions, usage examples, and detailed configuration explanations. The examples use creative scenarios from the banking domain to illustrate the tool's capabilities.
