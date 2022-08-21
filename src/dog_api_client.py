import json

import requests


class DogApiClient(object):
    def __init__(self):
        self._based_url = 'https://dog.ceo/api/'

    def list_all_breads(self, status_code: int = 200):
        url = f'{self._based_url}breed/hound/list'
        response = requests.request('GET', url)
        assert response.status_code == status_code, 'status code is unexpected'
        return json.loads(response.text)

    def random_image(self, multy_count: int = None, status_code: int = 200):
        url = f'{self._based_url}breeds/image/random'
        if multy_count:
            url = f'{url}/{multy_count}'
        response = requests.request('GET', url)
        assert response.status_code == status_code, 'status code is unexpected'
        return json.loads(response.text)

    def list_breads(self, bread: str, status_code: int = 200):
        url = f'{self._based_url}breed/{bread}/images/random'
        response = requests.request('GET', url)
        assert response.status_code == status_code, 'status code is unexpected'
        return json.loads(response.text)
