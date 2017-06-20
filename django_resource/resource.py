from .client import ResourceClient
from .manager import ResourceManager


class ResourceBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        parents = [b for b in bases if isinstance(b, ResourceBase)]
        if not parents:
            return new_class

        meta = attrs.pop('Meta', None)
        if meta is None:
            raise ValueError(
                "Resource {} must specify a Meta class defining at least "
                "the resource's main endpoints.".format(new_class.__name__)
            )

        if not meta.endpoints:
            raise ValueError(
                "Resource {} must specify a Meta class with attribute 'endpoints'.".format(new_class.__name__)
            )

        client_class = getattr(meta, 'client_class', ResourceClient)
        meta.client = client_class(endpoints=meta.endpoints)

        new_class._meta = meta
        new_class.objects = ResourceManager(resource_class=new_class)
        return new_class


class Resource(metaclass=ResourceBase):
    pass
