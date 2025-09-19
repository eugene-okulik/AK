import pytest


from test_api_kasymaliev_ak.methods.create_object import CreateObject
from test_api_kasymaliev_ak.methods.put_object import PutObject
from test_api_kasymaliev_ak.methods.patch_object import PatchObject
from test_api_kasymaliev_ak.methods.delete_object import DeleteObject


@pytest.fixture()
def create_new_object_fix():
    return CreateObject()


@pytest.fixture()
def object_for_test():
    obj = CreateObject()
    body = {"data": {"price": 350, "count": 1}, "name": "object for testing"}
    obj.post_object(body)
    object_id = obj.json["id"]
    return object_id


@pytest.fixture()
def updated_object_fix():
    return PutObject()


@pytest.fixture()
def patch_update_object_fix():
    return PatchObject()


@pytest.fixture()
def delete_object_fix():
    return DeleteObject()
