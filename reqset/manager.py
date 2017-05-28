from simple_model import model_builder

from .transports.requests import RequestsTransport


class ClientManager:
    def __init__(self, endpoint, client, transport_class=None):
        transport_class = transport_class or RequestsTransport
        self.endpoint = endpoint
        self.client = client
        self.headers = {'content_type': 'application/json'}
        self.transport = transport_class(headers=self.headers)

    @property
    def client_class_name(self):
        return self.client.__name__.replace('Client', '')

    def get(self, pk):
        endpoint = '{}/{}'.format(self.endpoint, pk)
        _, content = self.transport.request('GET', endpoint)
        return model_builder(content, self.client_class_name)
