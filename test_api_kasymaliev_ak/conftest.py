import pytest
import requests


from test_api_kasymaliev_ak.methods.create_object import CreateObject
from test_api_kasymaliev_ak.methods.put_object import PutObject
from test_api_kasymaliev_ak.methods.patch_object import PatchObject
from test_api_kasymaliev_ak.methods.delete_object import DeleteObject
from test_api_kasymaliev_ak.methods.get_object import GetObject


@pytest.fixture()
def create_new_object_fix():
    return CreateObject()


@pytest.fixture()
def create_test_object(create_new_object_fix):
    body = {"data": {"price": 350, "count": 1}, "name": "object for testing"}
    create_new_object_fix.post_object(body)
    object_id = create_new_object_fix.json["id"]
    post_body = create_new_object_fix.json
    yield post_body
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}",
                    headers=create_new_object_fix.headers)


@pytest.fixture()
def updated_object_fix():
    return PutObject()


@pytest.fixture()
def patch_update_object_fix():
    return PatchObject()


@pytest.fixture()
def delete_object_fix():
    return DeleteObject()


@pytest.fixture()
def get_object_fix():
    return GetObject()
