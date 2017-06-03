from reqset.resource import ResourceManager


def test_resource_construct(gist_resource):
    assert gist_resource.objects
    assert isinstance(gist_resource.objects, ResourceManager)
