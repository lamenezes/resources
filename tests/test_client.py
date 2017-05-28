from reqset.client import ClientManager


def test_client_construct(gist_client):
    assert gist_client.objects
    assert isinstance(gist_client.objects, ClientManager)
