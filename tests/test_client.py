from pytest import fixture

from pytest_easy_api.client import ApiClient


FLASK_PORT = 5000
BASE_URL = 'http://localhost:{port}'.format(port=FLASK_PORT)


# TODO: Add fixture to create/run app


@fixture(scope='module')
def api_client():
    """Create instance of the api client to use."""
    yield ApiClient(base_url=BASE_URL)


def test_get_request(api_client):
    """Verify GET request works using API client."""
    response = api_client.get('/get-test')
    assert response.url == '{base_url}/get-test'.format(base_url=BASE_URL)
    assert response.status_code == 200
    assert response.json() == {'Get-Test': 'A-OK'}


def test_post_request(api_client):
    """Verify POST request works using API client."""
    response = api_client.post('/post-test')
    assert response.url == '{base_url}/post-test'.format(base_url=BASE_URL)
    assert response.status_code == 200
    assert response.json() == {'Post-Test': 'A-OK'}


def test_put_request(api_client):
    """Verify PUT request works using API client."""
    response = api_client.put('/put-test')
    assert response.url == '{base_url}/put-test'.format(base_url=BASE_URL)
    assert response.status_code == 200
    assert response.json() == {'Put-Test': 'A-OK'}


def test_patch_request(api_client):
    """Verify PATCH request works using API client."""
    response = api_client.patch('/patch-test')
    assert response.url == '{base_url}/patch-test'.format(base_url=BASE_URL)
    assert response.status_code == 200
    assert response.json() == {'Patch-Test': 'A-OK'}


def test_delete_request(api_client):
    """Verify DELETE request works using API client."""
    response = api_client.delete('/delete-test')
    assert response.url == '{base_url}/delete-test'.format(base_url=BASE_URL)
    assert response.status_code == 200
    assert response.json() == {'Delete-Test': 'A-OK'}

