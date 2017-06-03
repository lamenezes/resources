from simple_model import model_builder

from .transports.requests import RequestsTransport


class ResourceManager:
    def __init__(self, endpoint, resource, transport_class=None):
        transport_class = transport_class or RequestsTransport
        self.endpoint = endpoint
        self.resource = resource
        self.headers = {'content_type': 'application/json'}
        self.transport = transport_class(headers=self.headers)

    @property
    def resource_class_name(self):
        return self.resource.__name__.replace('Resource', '')

    def get(self, pk, **kwargs):
        endpoint = '{}/{}'.format(self.endpoint, pk)
        _, content = self.transport.request('GET', endpoint, **kwargs)
        return model_builder(content, self.resource_class_name)

    def filter(self, **kwargs):
        _, content = self.transport.request('GET', self.endpoint, **kwargs)
        return model_builder(content, self.resource_class_name)
