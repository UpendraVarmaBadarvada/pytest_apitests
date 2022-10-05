import requests
import json
from requests.auth import HTTPBasicAuth


def test_create_user_method():
    post_url = "https://reqres.in/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(post_url, payload)
    assert response.status_code == 201


def test_get_user_method():
    get_url = "https://reqres.in/api/users?page=1"
    response = requests.get(get_url)
    print(response.content)
    print(response.headers)
    print(response.headers['Date'], response.headers['Server'])
    parsed_content = json.loads(response.text)
    print([data['email'] for data in parsed_content['data']])
    assert response.status_code == 200


def test_delete_user_method():
    delete_url = "https://reqres.in/api/users/2"
    response = requests.delete(delete_url)
    assert response.status_code == 204


def test_put_user_method():
    change_set = {
        "name": "morpheus",
        "job": "zion resident"
    }
    update_url = "https://reqres.in/api/users/2"
    response = requests.put(update_url, change_set)
    print(response.text)
    assert response.status_code == 200


def test_custom_headers_method():
    header_data = {
        'Authorization': 'Bearer token_value'
    }
    response = requests.get('https://httpbin.org/get', headers=header_data)
    print(json.loads(response.text))


def test_query_params_method():
    params = {
        'name': 'Upendra',
        'email': 'upendravarma1993@gmail.com',
        'number': '8886183899'
    }
    response = requests.get('https://httpbin.org/get', params=params)
    print(response.text)


def test_authentication_method():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('UpendraVarmaBadarvada', 'ILovePython@9'))
    assert response.status_code == 401


