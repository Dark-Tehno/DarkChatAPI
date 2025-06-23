import requests


def _api_request(method, url, headers=None, json_data=None):
    """
    A helper function to make API requests and handle responses consistently.
    Returns a tuple of (data, status_code).
    On network errors, returns (error_message, -1).
    """
    try:
        response = requests.request(method, url, headers=headers, json=json_data)
        if response.status_code == 200:
            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError:
                data = response.text
            return data, response.status_code
        return response.text, response.status_code
    except requests.RequestException as e:
        return str(e), -1