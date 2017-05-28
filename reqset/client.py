from .manager import ClientManager


class ClientBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        parents = [b for b in bases if isinstance(b, ClientBase)]
        if not parents:
            return new_class

        new_class.objects = ClientManager(
            endpoint=attrs.pop('endpoint'),
            client=new_class,
            transport_class=attrs.pop('transport_class', None),
        )
        return new_class


class Client(metaclass=ClientBase):
    pass
