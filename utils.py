import requests


def fetch_data(endpoint):
    # endpoint can be path to json file or url, return data with succcess or failure
    if endpoint.startswith('http'):
        response = fetch_data_from_url(endpoint)
        return response.json(), response.status_code
    else:
        return fetch_data_from_file(endpoint), 200


def fetch_data_from_url(url):
    return requests.get(url)

def fetch_data_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

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
