import json

import requests


class OpenBreweryDBClient(object):
    def __init__(self):
        self._based_url = 'https://api.openbrewerydb.org/breweries/'

    def list_breweries(self, params: dict = None, status_code: int = 200):
        response = requests.request('GET', self._based_url, params=params)
        assert response.status_code == status_code, 'status code is unexpected'
        return json.loads(response.text)
