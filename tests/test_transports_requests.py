from unittest import mock

import pytest

from reqset.transports.requests import RequestsTransport

from .vcr import vcr


@pytest.fixture()
def requests_transport():
    return RequestsTransport()


def test_requests_transport_extract_response_data(requests_transport):
    mock_response = mock.Mock()

    requests_transport._extract_response_data(mock_response)

    mock_response.json.assert_called_with()


def test_requests_transport_extract_response_status(requests_transport):
    expected_status = 200
    mock_response = mock.Mock(status_code=expected_status)

    status = requests_transport._extract_response_status_code(mock_response)

    assert status == expected_status


@vcr.use_cassette()
def test_requests_transport_request(httpbin_url, requests_transport):
    url = '{}get?foo=bar'.format(httpbin_url)

    response = requests_transport._request('get', url)

    assert response.status_code == 200
    content = response.json()
    assert content['args']['foo'] == 'bar'
    response.connection.close()
