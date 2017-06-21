from unittest import mock

from simple_model import Model


def test_resource_manager_resource_class_name(gist_resource_manager):
    assert gist_resource_manager.resource_class_name == 'Gist'


def test_resource_manager_resource_client(gist_resource_manager):
    assert gist_resource_manager.client


def test_resource_manager_build_model(gist_resource_manager):
    resource = gist_resource_manager._build_model({})
    assert isinstance(resource, Model)


@mock.patch('django_resource.manager.ResourceManager.client')
def test_resource_manager_get(mock_client, gist_resource_manager, gist_id, gist_data):
    mock_client.get.return_value = gist_data

    gist = gist_resource_manager.get(gist_id)
    assert gist.id == gist_id

    mock_client.get.assert_called_with(gist_id)


@mock.patch('django_resource.manager.ResourceManager.client')
def test_resource_manager_filter(mock_client, gist_resource_manager, gist_data):
    mock_client.filter.return_value = [gist_data] * 2
    kwargs = {'foo': 'bar', 'baz': 'qux'}

    gist = gist_resource_manager.filter(**kwargs)
    assert len(gist) == 2

    mock_client.filter.assert_called_with(**kwargs)


@mock.patch('django_resource.manager.ResourceManager.client')
def test_resource_manager_all(mock_client, gist_resource_manager, gist_data):
    mock_client.filter.return_value = [gist_data] * 2

    gist = gist_resource_manager.all()
    assert len(gist) == 2

    mock_client.filter.assert_called_with()


@mock.patch('django_resource.manager.ResourceManager.client')
def test_resource_manager_create(mock_client, gist_resource_manager, gist_id, gist_data):
    mock_client.post.return_value = gist_data

    gist = gist_resource_manager.create(**gist_data)
    assert gist.id == gist_id

    mock_client.post.assert_called_with(**gist_data)


@mock.patch('django_resource.manager.ResourceManager.client')
def test_resource_manager_update(mock_client, gist_resource_manager, gist_id, gist_data):
    mock_client.patch.return_value = gist_data

    gist = gist_resource_manager.update(gist_id, **gist_data)
    assert gist.id == gist_id

    mock_client.patch.assert_called_with(gist_id, **gist_data)


@mock.patch('django_resource.manager.ResourceManager.client')
def test_resource_manager_create_or_update(mock_client, gist_resource_manager, gist_id, gist_data):
    mock_client.put.return_value = gist_data

    gist = gist_resource_manager.create_or_update(gist_id, **gist_data)
    assert gist.id == gist_id

    mock_client.put.assert_called_with(gist_id, **gist_data)


@mock.patch('django_resource.manager.ResourceManager.client')
def test_resource_manager_delete(mock_client, gist_resource_manager, gist_id):
    assert gist_resource_manager.delete(gist_id) is None

    mock_client.delete.assert_called_with(gist_id)
