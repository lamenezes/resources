import requests

from .base import BaseTransport


class RequestsTransport(BaseTransport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = requests.Session()

    def _request(self, method, endpoint, **kwargs):
        method = getattr(self.session, method)
        response = method(endpoint, **kwargs)
        return response

    def _extract_response_data(self, response):
        return response.json()

    def _extract_response_status_code(self, response):
        return response.status_code
