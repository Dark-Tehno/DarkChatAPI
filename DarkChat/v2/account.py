from .utils import _api_request

BASE_URL = 'https://vsp210.ru/api/v2/'


def login(username, password):
    url = f'{BASE_URL}login/'
    json_data = {
        'username': username,
        'password': password
    }
    data, status_code = _api_request('post', url, json_data=json_data)
    if status_code == 200 and isinstance(data, dict):
        return data.get('token'), status_code
    return data, status_code


def register(username, email, password):
    url = f'{BASE_URL}register/'
    json_data = {
        'username': username,
        'email': email,
        'password': password
    }
    data, status_code = _api_request('post', url, json_data=json_data)
    if status_code == 200 and isinstance(data, dict):
        return data.get('token'), status_code
    return data, status_code


def logout(token):
    url = f'{BASE_URL}logout/'
    headers = {'Authorization': f'Token {token}'}
    return _api_request('post', url, headers=headers)


def my_data(token):
    url = f'{BASE_URL}my-data/'
    headers = {'Authorization': f'Token {token}'}
    return _api_request('post', url, headers=headers)


def user_data(username):
    url = f'{BASE_URL}user-data/{username}/'
    return _api_request('get', url)


def search(token, query):
    url = f'{BASE_URL}search/'
    headers = {'Authorization': f'Token {token}'}
    json_data = {
        'q': query
    }
    return _api_request('post', url, headers=headers, json_data=json_data)