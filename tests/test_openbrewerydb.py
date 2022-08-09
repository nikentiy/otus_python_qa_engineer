import pytest


def test_list_breweries(openbrewerydb_client):
    data = openbrewerydb_client.list_breweries()
    assert len(data) == 20, 'List of breweries has not default length'


@pytest.mark.parametrize("brewery_type", ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar',
                                          'contract', 'proprietor', 'closed'])
def test_filter_by_type_list_breweries(openbrewerydb_client, brewery_type):
    data = openbrewerydb_client.list_breweries(params={'by_type': brewery_type})
    assert all(brewery['brewery_type'] == brewery_type for brewery in data), \
        f'some items in the list is in unexpected type {brewery_type}'


def test_unsupported_by_type_filter_list_breweries(openbrewerydb_client):
    data = openbrewerydb_client.list_breweries(params={'by_type': 'test'}, status_code=400)
    assert 'Brewery type must include one of these types' in data['errors'][0]


@pytest.mark.parametrize("pages", [0, 1, 25, 49, 50])
def test_filter_per_page_list_breweries(openbrewerydb_client, pages):
    data = openbrewerydb_client.list_breweries(params={'per_page': pages})
    assert len(data) == pages


@pytest.mark.parametrize("pages", [-1, 'one', 51])
def test_ignoring_wrong_filter_per_page_list_breweries(openbrewerydb_client, pages):
    data = openbrewerydb_client.list_breweries(params={'per_page': pages})
    assert len(data) in [20, 50]
