import pytest


@pytest.mark.parametrize("resource", [
    {'title': 'big QA', 'body': "that's the way", 'userId': 50},
    {'story': "a long time ago I met an young man", 'name': "bro", 'contents': ['first visit', 'big friendship']},
    {'capitals': {'Russia': 'Moscow', 'Cyprus': 'Nicosia', 'UAR': 'Cape Town'}},
    ])
def test_create_resource(jsonplaceholder_client, resource):
    data = jsonplaceholder_client.create_resource(data=resource)
    assert all(k in data and data[k] == v for k, v in resource.items()), \
        "created resource doesn't match to the provided one"


@pytest.mark.parametrize("resource", [1, 'test', None])
def test_negative_create_resource(jsonplaceholder_client, resource):
    jsonplaceholder_client.create_resource(data=resource, status_code=400)


@pytest.mark.parametrize("new_data", [{'km': 100}, {'stops': ['Minsk', 'Smolensk', 'Moscow']}, {'price': 'undefined'}])
def test_updating_resource(jsonplaceholder_client, created_resource, new_data):
    resource = created_resource.update(new_data)
    data = jsonplaceholder_client.update_resource(resource_id=created_resource['id'], data=resource)
    assert all(k in data and data[k] == v for k, v in resource.items()), \
        "updated resource doesn't match to the provided one"


@pytest.mark.parametrize("new_data", [1, 'test', None])
def test_negative_updating_resource(jsonplaceholder_client, created_resource, new_data):
    jsonplaceholder_client.update_resource(resource_id=created_resource['id'], data=new_data, status_code=400)


def test_updating_not_existing_resource(jsonplaceholder_client, created_resource):
    jsonplaceholder_client.update_resource(resource_id=1001, data=created_resource, status_code=404)
