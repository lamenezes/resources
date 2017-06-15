from unittest import mock

import pytest
from staty.exceptions import (
    ClientErrorException,
    ServerErrorException,
    UnauthorizedException,
)

from django_resource.client import ResourceClient

from .vcr import vcr


@pytest.fixture
def client(gist_resource):
    return ResourceClient(gist_resource.endpoint)


@pytest.fixture
def mock_client(client):
    client.request = mock.Mock()
    return client


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


def test_resource_client_get_endpoint(mock_client):
    assert mock_client.get_endpoint() == mock_client._endpoint


def test_resource_client_get_endpoint_with_pk(mock_client, gist_id):
    endpoint = mock_client.get_endpoint(gist_id)
    assert mock_client._endpoint in endpoint
    assert gist_id in endpoint


def test_resource_client_get(mock_client, gist_id):
    mock_client.get(gist_id)

    endpoint = mock_client.get_endpoint(gist_id)
    mock_client.request.assert_called_with('GET', endpoint)


@pytest.mark.parametrize(('method', 'verb'), (
    ('fetch', 'GET'),
    ('create', 'POST'),
    ('create_or_update', 'PUT'),
))
def test_resource_client_requests_without_pk(method, verb, mock_client):
    method = getattr(mock_client, method)

    method()

    mock_client.request.assert_called_with(verb, mock_client.get_endpoint())


@pytest.mark.parametrize(('method', 'verb'), (
    ('get', 'GET'),
    ('patch', 'PATCH'),
))
def test_resource_client_requests_with_pk(method, verb, mock_client, gist_id):
    method = getattr(mock_client, method)
    data = {'foo': 'bar'}

    method(gist_id, **data)

    mock_client.request.assert_called_with(verb, mock_client.get_endpoint(gist_id), **data)


@pytest.mark.parametrize(('status_codes', 'exception'), (
    (range(400, 500), ClientErrorException),
    (range(500, 531), ServerErrorException),
    ((401, 403), UnauthorizedException),
))
def test_resource_client_raise_for_status(status_codes, exception, mock_client):
    for status_code in status_codes:
        with pytest.raises(exception):
            mock_client.raise_for_status(None, status_code)
