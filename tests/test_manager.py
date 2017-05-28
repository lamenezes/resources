from unittest import mock


def test_client_manager_client_class_name(gist_client_manager):
    assert gist_client_manager.client_class_name == 'Gist'


@mock.patch('reqset.manager.RequestsTransport.request')
def test_client_manager_get(mock_request, gist_client_manager, gist_id, gist_data):
    mock_request.return_value = (None, gist_data)

    gist = gist_client_manager.get(pk=gist_id)
    assert gist.id == gist_id
