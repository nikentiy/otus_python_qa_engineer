import pytest
import requests


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def test_request(url, status_code):
    response = requests.request('GET', url)
    assert response.status_code == status_code, f'status code is unexpected. Expected: {status_code}, ' \
                                                f'Actual: {response.status_code}'
