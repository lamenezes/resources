import pytest

from django_resource.resource import Resource, ResourceManager


def test_resource_construct(gist_resource):
    assert gist_resource.objects
    assert isinstance(gist_resource.objects, ResourceManager)


def test_resource_construct_without_meta(gist_resource):
    with pytest.raises(ValueError) as exc:
        class InvalidResource(Resource):
            pass

    assert 'must specify a Meta class' in str(exc)


def test_resource_construct_invalid_meta(gist_resource):
    with pytest.raises(ValueError) as exc:
        class InvalidResource(Resource):
            class Meta:
                pass

    assert 'Meta class must have' in str(exc)
