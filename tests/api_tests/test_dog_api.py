import pytest

from src.helper import is_string_url


def test_list_all_breads(dog_client):
    data = dog_client.list_all_breads()
    assert len(data["message"]) != 0, 'List of all breads is empty'


@pytest.mark.parametrize("number", [None, 0, 1, 2, 15])
def test_random_image(dog_client, number):
    data = dog_client.random_image(number)
    if not number:
        assert data["message"]
    else:
        assert len(data["message"]) == number


@pytest.mark.parametrize("number", ['one', 'hello'])
def test_failure_random_image(dog_client, number):
    dog_client.random_image(number, 404)


@pytest.mark.parametrize("bread", ['affenpinscher', 'mix', 'wolfhound/irish'])
def test_list_breads(dog_client, bread):
    data = dog_client.list_breads(bread)
    assert is_string_url(data['message'])


@pytest.mark.parametrize("bread", ['Whippeture', 10])
def test_not_existing_bread(dog_client, bread):
    data = dog_client.list_breads(bread, 404)
    assert 'Breed not found' in data['message']
