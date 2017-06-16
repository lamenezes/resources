from unittest import mock

from simple_model import Model


def test_resource_manager_resource_class_name(gist_resource_manager):
    assert gist_resource_manager.resource_class_name == 'Gist'


def test_resource_manager_build_model(gist_resource_manager):
    resource = gist_resource_manager._build_model({})
    assert isinstance(resource, Model)


@mock.patch('django_resource.client.ResourceClient.request')
def test_resource_manager_get(mock_request, gist_resource_manager, gist_id, gist_data):
    mock_request.return_value = gist_data

    gist = gist_resource_manager.get(pk=gist_id)
    assert gist.id == gist_id

    assert mock_request.called


@mock.patch('django_resource.client.ResourceClient.request')
def test_resource_manager_filter(mock_request, gist_resource_manager, gists_data):
    mock_request.return_value = gists_data

    gists = gist_resource_manager.filter()
    assert len(gists) == 2
    for gist in gists:
        assert isinstance(gist, Model)

    assert mock_request.called
