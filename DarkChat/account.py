import requests

BASE_URL = 'https://vsp210.ru/api/v1/'


def login(username, password):
    url = f'{BASE_URL}login/'
    data = {
        'username': username,
        'password': password
        }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        token = response.json().get('token')
        return token, response.status_code
    else:
        return response.status_code, response.text



def register(username, email, password):
    url = f'{BASE_URL}register/'
    data = {
        'username': username,
        'email': email,
        'password': password
        }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        token = response.json().get('token')
        return token, response.status_code
    else:
        return response.status_code, response.text


def logout(token):
    url = f'{base_url}logout/'
    response = requests.post(url, data={'token': token})
    if response.status_code == 200:
        return 'Logged out successfully', response.status_code
    else:
        return response.status_code, response.text



def my_data(token):
    url = f'{base_url}my-data/'
    response = requests.post(url, data={'token': token})
    if response.status_code == 200:
        data = response.json()
        return data, response.status_code
    else:
        return response.status_code, response.text



def user_data(username):
    url = f'{BASE_URL}user-data/{username}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data, response.status_code
    else:
        return response.status_code, response.text
