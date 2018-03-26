from pytest import fixture

from pytest_easy_api.client import ApiClient


@fixture(scope='module')
def api(request):
    """Fixture to return the API Client.

    You can then use it inside you test like:

    ..code-block::python

        def test_my_get_request(api):
            response = api.get('/my-endpoint')
            assert response.status_code == 200

    """
    # TODO: Add hook to read base url from custom location
    # not just on the command line
    url = request.config.getoption('base_url')
    yield ApiClient(base_url=url)


def pytest_addoption(parser):
    """Add `base_url` option to specify the url to run tests against."""
    group = parser.getgroup('pytest_easy_api')
    group.addoption('--base_url', action='store', dest='base_url',
                    default=None, help='Base url to run tests against.')
