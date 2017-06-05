from simple_model import model_builder

from .client import ResourceClient


class ResourceManager:
    def __init__(self, endpoint, resource, client_class=ResourceClient):
        self.resource = resource
        headers = {'content_type': 'application/json'}
        self.client = client_class(endpoint=endpoint, headers=headers)

    @property
    def resource_class_name(self):
        return self.resource.__name__.replace('Resource', '')

    def _build_model(self, content):
        return model_builder(content, self.resource_class_name)

    def get(self, pk, **kwargs):
        return self.client.get(pk, **kwargs)

    def filter(self, **kwargs):
        return self.client.fetch(**kwargs)

    def create(self, **kwargs):
        return self.client.post(**kwargs)

    def update(self, pk, **kwargs):
        return self.client.patch(pk, **kwargs)

    def create_or_update(self, pk, **kwargs):
        return self.client.put(pk, **kwargs)
