import json

import requests


class JsonPlaceholderClient(object):
    def __init__(self):
        self._based_url = 'https://jsonplaceholder.typicode.com/'

    def create_resource(self, data: dict, status_code: int = 201):
        url = f'{self._based_url}posts'
        response = requests.request('POST', url, json=data)
        assert response.status_code == status_code, f'status code is unexpected. Expected: {status_code}, ' \
                                                    f'Actual: {response.status_code}'
        return json.loads(response.text)

    def update_resource(self, resource_id: int, data: dict, status_code: int = 200):
        url = f'{self._based_url}posts/{resource_id}'
        response = requests.request('PUT', url, json=data)
        assert response.status_code == status_code, f'status code is unexpected. Expected: {status_code}, ' \
                                                    f'Actual: {response.status_code}'
        return json.loads(response.text)
