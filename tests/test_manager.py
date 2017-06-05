from unittest import mock


def test_resource_manager_resource_class_name(gist_resource_manager):
    assert gist_resource_manager.resource_class_name == 'Gist'


@mock.patch('reqset.client.ResourceClient.request')
def test_resource_manager_get(mock_request, gist_resource_manager, gist_id, gist_data):
    mock_request.return_value = gist_data

    gist = gist_resource_manager.get(pk=gist_id)
    assert gist['id'] == gist_id
