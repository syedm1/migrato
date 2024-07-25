import requests

def fetch_data(endpoint):
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()

def remove_ignored_keys(data, ignore_keys):
    if not ignore_keys:
        return data
    if isinstance(data, dict):
        return {k: remove_ignored_keys(v, ignore_keys) for k, v in data.items() if k not in ignore_keys}
    elif isinstance(data, list):
        return [remove_ignored_keys(item, ignore_keys) for item in data]
    else:
        return data

def get_nested_value(data, keys):
    for key in keys.split('.'):
        data = data[key]
    return data
