import requests
from staty.exceptions import (
    ClientErrorException,
    ServerErrorException,
    UnauthorizedException,
)


class ResourceClient:
    def __init__(self, endpoints, headers=None):
        self._endpoints = endpoints
        headers = headers or {'content_type': 'application/json'}
        self.session = requests.Session()
        self.session.headers.update(headers)

    def raise_for_status(self, response, status_code, *args, **kwargs):
        message = '{}: {}'.format(status_code, response.text)
        if status_code in (401, 403):
            raise UnauthorizedException(message, *args, response=response, **kwargs)
        if status_code in range(400, 500):
            raise ClientErrorException(message, *args, response=response, **kwargs)
        if status_code in range(500, 600):
            raise ServerErrorException(message, *args, response=response, **kwargs)

    def request(self, method, endpoint, **kwargs):
        method = method.lower()
        method = getattr(self.session, method)
        response = method(endpoint, **kwargs)
        self.raise_for_status(response, response.status_code)
        if 200 <= response.status_code < 300:
            return response.json()
        return response.text()

    def get_endpoint(self, method, pk=None):
        endpoint = self._endpoints[method]
        if pk is None:
            return endpoint

        return '{}/{}'.format(endpoint, pk)

    def get(self, pk, **kwargs):
        endpoint = self.get_endpoint('get', pk)
        return self.request('GET', endpoint, **kwargs)

    def filter(self, **kwargs):
        endpoint = self.get_endpoint('filter')
        return self.request('GET', endpoint, **kwargs)

    def post(self, **kwargs):
        endpoint = self.get_endpoint('post')
        return self.request('POST', endpoint, **kwargs)

    def patch(self, pk, **kwargs):
        endpoint = self.get_endpoint('patch', pk)
        return self.request('PATCH', endpoint, **kwargs)

    def put(self, **kwargs):
        endpoint = self.get_endpoint('put')
        return self.request('PUT', endpoint, **kwargs)

    def delete(self, pk, **kwargs):
        endpoint = self.get_endpoint('delete', pk)
        return self.request('PUT', endpoint, **kwargs)
