import pytest

from reqset.transports.base import BaseTransport


@pytest.fixture
def transport():
    class Transport(BaseTransport):
        def _request(self, method, endpoint, headers, **kwargs):
            return True

        def _extract_response_data(self, response):
            return {'foo': 'bar'}

    return Transport()


@pytest.fixture
def wrong_transport():
    class WrongTransport(BaseTransport):
        pass
    return WrongTransport()


def test_transport(transport, fetch_url):
    response, content = transport.request('GET', fetch_url)
    assert content == {'foo': 'bar'}
    assert response is True


def test_wrong_transport(wrong_transport):
    with pytest.raises(NotImplementedError):
        wrong_transport._request(None, None, None)

    with pytest.raises(NotImplementedError):
        wrong_transport._extract_response_data(None)
