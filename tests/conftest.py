import pytest

from src.circle import Circle
from src.dog_api_client import DogApiClient
from src.jsonplaceholder_client import JsonPlaceholderClient
from src.openbrewerydb_api_client import OpenBreweryDBClient
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture(scope='class')
def triangle():
    return Triangle(14, 13.5, 5)


@pytest.fixture(scope='class')
def rectangle():
    return Rectangle(14, 5)


@pytest.fixture(scope='class')
def square():
    return Square(5.3)


@pytest.fixture(scope='class')
def circle():
    return Circle(9.1)


@pytest.fixture(scope='class')
def dog_client():
    return DogApiClient()


@pytest.fixture(scope='class')
def openbrewerydb_client():
    return OpenBreweryDBClient()


@pytest.fixture(scope='class')
def jsonplaceholder_client():
    return JsonPlaceholderClient()


@pytest.fixture(scope='function')
def created_resource(jsonplaceholder_client):
    resource = {'way': 'the is no way'}
    return jsonplaceholder_client.create_resource(data=resource)
