import requests

BASE_URL = 'https://vsp210.ru/api/v2/'


def login(username, password):
    url = f'{BASE_URL}login/'
    data = {
        'username': username,
        'password': password
        }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        token = response.json().get('token')
        return token, response.status_code
    else:
        return response.text, response.status_code



def register(username, email, password):
    url = f'{BASE_URL}register/'
    data = {
        'username': username,
        'email': email,
        'password': password
        }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        token = response.json().get('token')
        return token, response.status_code
    else:
        return response.text, response.status_code


def logout(token):
    url = f'{BASE_URL}logout/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return 'Logged out successfully', response.status_code
    else:
        return response.text, response.status_code



def my_data(token):
    url = f'{BASE_URL}my-data/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data, response.status_code
    else:
        return response.text, response.status_code



def user_data(username):
    url = f'{BASE_URL}user-data/{username}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data, response.status_code
    else:
        return response.text, response.status_code


def search(token, query):
    url = f'{BASE_URL}search/'
    headers = {'Authorization': f'Token {token}'}
    data = {
        'q': query
        }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data, response.status_code
    else:
        return response.text, response.status_code