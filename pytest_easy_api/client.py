from requests import Session


class ApiClient(Session):

    def __init__(self, base_url):
        super(ApiClient, self).__init__()
        self.base_url = base_url

    def _build_url(self, extension):
        return '{base_url}{extension}'.format(
            base_url=self.base_url, extension=extension)

    def get(self, url, **kwargs):
        _url = self._build_url(extension=url)
        return super(ApiClient, self).get(_url, **kwargs)

    def post(self, url, **kwargs):
        _url = self._build_url(extension=url)
        return super(ApiClient, self).post(_url, **kwargs)

    def put(self, url, **kwargs):
        _url = self._build_url(extension=url)
        return super(ApiClient, self).put(_url, **kwargs)

    def patch(self, url, **kwargs):
        _url = self._build_url(extension=url)
        return super(ApiClient, self).patch(_url, **kwargs)

    def delete(self, url, **kwargs):
        _url = self._build_url(extension=url)
        return super(ApiClient, self).delete(_url, **kwargs)
