from unittest import TestCase
import requests


class ApiAuthTestCase(TestCase):
    def test_create_token(self):
        username = 'admin'
        password = '1234'
        url = 'http://127.0.0.1:8000/api-token-auth/'
        json = {
            'username': username,
            'password': password
        }
        res = requests.post(url, json=json)

        print(res)
        print(res.json())
