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
        return model_builder(data=content, class_name=self.resource_class_name)

    def get(self, pk, **kwargs):
        resource = self.client.get(pk, **kwargs)
        return self._build_model(resource)

    def filter(self, **kwargs):
        content = self.client.fetch(**kwargs)
        return [self._build_model(resource) for resource in content]

    def create(self, **kwargs):
        resource = self.client.post(**kwargs)
        return self._build_model(resource)

    def update(self, pk, **kwargs):
        content = self.client.patch(pk, **kwargs)
        return self._build_model(content)

    def create_or_update(self, pk, **kwargs):
        content = self.client.put(pk, **kwargs)
        return self._build_model(content)
