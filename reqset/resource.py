from .manager import ResourceManager


class ResourceBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        parents = [b for b in bases if isinstance(b, ResourceBase)]
        if not parents:
            return new_class

        new_class.objects = ResourceManager(
            endpoint=attrs.pop('endpoint'),
            resource=new_class,
        )
        return new_class


class Resource(metaclass=ResourceBase):
    pass
