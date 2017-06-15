import requests
from staty.exceptions import (
    ClientErrorException,
    ServerErrorException,
    UnauthorizedException,
)


class ResourceClient:
    def __init__(self, endpoint, headers=None):
        self._endpoint = endpoint
        headers = headers or {'content_type': 'application/json'}
        self.session = requests.Session()
        self.session.headers.update(headers)

    def raise_for_status(self, response, status_code, *args, **kwargs):
        if status_code in (401, 403):
            raise UnauthorizedException(*args, **kwargs, response=response)
        if status_code in range(400, 500):
            raise ClientErrorException(*args, **kwargs, response=response)
        if status_code in range(500, 600):
            raise ServerErrorException(*args, **kwargs, response=response)

    def request(self, method, endpoint, **kwargs):
        method = method.lower()
        method = getattr(self.session, method)
        response = method(endpoint, **kwargs)
        self.raise_for_status(response, response.status_code)
        if 200 <= response.status_code < 300:
            return response.json()
        return response.text()

    def get_endpoint(self, pk=None):
        if pk is None:
            return self._endpoint

        return '{}/{}'.format(self._endpoint, pk)

    def get(self, pk, **kwargs):
        endpoint = self.get_endpoint(pk)
        return self.request('GET', endpoint, **kwargs)

    def fetch(self, **kwargs):
        endpoint = self.get_endpoint()
        return self.request('GET', endpoint, **kwargs)

    def create(self, **kwargs):
        endpoint = self.get_endpoint()
        return self.request('POST', endpoint, **kwargs)

    def patch(self, pk, **kwargs):
        endpoint = self.get_endpoint(pk)
        return self.request('PATCH', endpoint, **kwargs)

    def create_or_update(self, **kwargs):
        endpoint = self.get_endpoint()
        return self.request('PUT', endpoint, **kwargs)
