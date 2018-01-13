from unittest import mock

import pytest
from staty.exceptions import (
    ClientErrorException,
    ServerErrorException,
    UnauthorizedException,
)

from resources.client import ResourceClient

from .vcr import vcr


@pytest.fixture
def client(gist_resource):
    return ResourceClient(gist_resource._meta.endpoints)


@pytest.fixture
def mock_client(client):
    client.request = mock.Mock()
    return client


@pytest.fixture
def mock_response():
    return mock.Mock(text='errow')


@vcr.use_cassette()
def test_resource_client_request(client, gist_id):
    gist = client.get(gist_id)
    assert gist['id'] == gist_id
    assert 'files' in gist


def test_resource_client_request_response_redirect(client, gist_id):
    client.session = mock.Mock()
    client.session.get.return_value = mock.Mock(status_code=300, text=lambda: 'birl')

    response = client.get(gist_id)

    assert response == 'birl'


@pytest.mark.parametrize('method', ('filter', 'post', 'put'))
def test_resource_client_get_endpoint(method, mock_client):
    assert mock_client.get_endpoint(method) == mock_client._endpoints[method]


@pytest.mark.parametrize('method', ('delete', 'get', 'patch'))
def test_resource_client_get_endpoint_with_pk(method, mock_client, gist_id):
    endpoint = mock_client.get_endpoint(method, gist_id)
    assert mock_client._endpoints[method][:-3] in endpoint
    assert gist_id in endpoint


def test_resource_client_get(mock_client, gist_id):
    mock_client.get(gist_id)

    endpoint = mock_client.get_endpoint('get', gist_id)
    mock_client.request.assert_called_with('GET', endpoint)


def test_resource_client_requests_post(mock_client):
    kwargs = {'foo': 'oo', 'bar': 'ar'}

    mock_client.post(**kwargs)

    endpoint = mock_client.get_endpoint('post')
    mock_client.request.assert_called_with('POST', endpoint, json=kwargs)


@pytest.mark.parametrize(('method_name', 'verb'), (
    ('filter', 'GET'),
    ('put', 'PUT'),
))
def test_resource_client_requests_without_pk(method_name, verb, mock_client):
    kwargs = {'foo': 'oo', 'bar': 'ar'}
    method = getattr(mock_client, method_name)

    method(**kwargs)

    endpoint = mock_client.get_endpoint(method_name)
    mock_client.request.assert_called_with(verb, endpoint, **kwargs)


@pytest.mark.parametrize(('method_name', 'verb'), (
    ('delete', 'DELETE'),
    ('get', 'GET'),
    ('patch', 'PATCH'),
))
def test_resource_client_requests_with_pk(method_name, verb, mock_client, gist_id):
    method = getattr(mock_client, method_name)
    data = {'foo': 'bar'}

    method(gist_id, **data)

    endpoint = mock_client.get_endpoint(method_name, gist_id)
    expected_kwargs = {'json': data} if verb == 'PATCH' else data
    mock_client.request.assert_called_with(verb, endpoint, **expected_kwargs)


@pytest.mark.parametrize(('status_codes', 'exception'), (
    (range(400, 500), ClientErrorException),
    (range(500, 531), ServerErrorException),
    ((401, 403), UnauthorizedException),
))
def test_resource_client_raise_for_status(status_codes, exception, mock_client, mock_response):
    for status_code in status_codes:
        with pytest.raises(exception) as exc:
            mock_client.raise_for_status(mock_response, status_code)

        assert exc.value.response == mock_response
        assert str(status_code) in str(exc)
        assert mock_response.text in str(exc)
