class BaseTransport:
    def __init__(self, headers=None):
        self.headers = headers or {}

    def _request(self, method, endpoint, headers, **kwargs):
        raise NotImplementedError('_request must be overriden')

    def _extract_response_data(self, response):
        raise NotImplementedError('_extract_response_data must be overriden')

    def request(self, method, endpoint, **kwargs):
        method = method.lower()
        response = self._request(method, endpoint, headers=self.headers, **kwargs)
        return response, self._extract_response_data(response)
