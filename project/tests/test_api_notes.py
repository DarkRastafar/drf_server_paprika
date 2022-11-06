import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from unittest import TestCase
import requests


class ApiNotesTestCase(TestCase):
    def setUp(self) -> None:
        self.HEADERS = {'Authorization': 'Token 6c4a0e4d6aa4a50dbc8e35329affe610747c120d'}

    def test_add_note(self):
        json_data = {
            'label': 'Новая запись',
            'body': 'Абракадабра Абракадабра Абракадабра Абракадабра Абракадабра Абракадабра Абракадабра',
            'notebook': 1,
            'user': 1
        }

        res = requests.post(f'http://127.0.0.1:8000/api/notes/note/', json=json_data, headers=self.HEADERS)
        print(res)
        # print(res.json())

    def test_put_note(self):
        json_data = {
            'label': 'Тестовая запись',
            'body': 'Абракадабра Абракадабра Абракадабра',
            'notebook': None,
            'user': 1
        }
        res = requests.put(f'http://127.0.0.1:8000/api/notes/note/10/', json=json_data, headers=self.HEADERS)
        print(res)


