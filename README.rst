Pytest Easy Api
===============

*A pytest plugin for super simple API testing.*

Using the `api` fixture
-----------------------
The `api` fixture, acts as a pass through to a `requests.Session` object, 
meaning you can make your API calls from it like so:

.. code-block:: python

    def test_my_get_function(api):
        response = api.get('/my-get-endpoint')
        assert response.status_code == 200


Anything you can usually do through `requests.Session` you can do through this 
fixture, but you only need to pass the url extension, meaning you can run these
same tests on any running instance of your application. 


TODO
----
1. Add option to read base url from config.
2. Tests.
3. Add documentation.
4. Add decorator to read mock from json file.

