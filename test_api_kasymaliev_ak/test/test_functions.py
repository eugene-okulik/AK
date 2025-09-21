import pytest
import allure


data = [{"data": {"price": 150, "count": 1}, "id": 1, "name": "Test object"},
        {"data": {"price": 300, "count": 2}, "id": 1, "name": "Test object_2"},
        {"data": {"price": 450, "count": 3}, "id": 1, "name": "Test object_3"}]


@allure.feature('Create_object')
@allure.story('CRUD')
@pytest.mark.pozitive
@pytest.mark.parametrize('body', data)
def test_post_object(create_new_object_fix, body):  # Проверка POST
    create_new_object_fix.post_object(body)
    create_new_object_fix.check_statuscode_is_200()
    create_new_object_fix.check_price(body["data"]["price"])
    create_new_object_fix.check_count(body["data"]["count"])
    create_new_object_fix.check_name(body["name"])


data_negative = [{"data": "", "id": 1, "name": "Test object"},
                 {"data": {"price": 450, "count": 3}, "id": 1},
                 {"id": 1, "name": "Test object_3"}]


@allure.feature('Create_object')
@allure.story('CRUD')
@pytest.mark.negative
@pytest.mark.parametrize('body', data_negative)
def test_post_object_negative(create_new_object_fix, body):
    create_new_object_fix.post_object(body)
    create_new_object_fix.check_statuscode_is_400()


@allure.feature('Update_object')
@allure.story('CRUD')
@pytest.mark.pozitive
def test_put_object(create_test_object, updated_object_fix):  # Проверка PUT
    object_id = create_test_object["id"]
    body = {
        "data": {"price": 300,
                 "count": 2},
        "id": object_id,
        "name": "Test object version 1"
    }
    updated_object_fix.put_object(body, object_id)
    updated_object_fix.check_statuscode_is_200()
    updated_object_fix.check_object_id(body['id'])
    updated_object_fix.check_price(body['data']['price'])
    updated_object_fix.check_count(body['data']['count'])
    updated_object_fix.check_name(body['name'])


@allure.feature('Patch_update_object')
@allure.story('CRUD')
@pytest.mark.pozitive
def test_patch_object(create_test_object, patch_update_object_fix):  # Проверка PATCH
    object_id = create_test_object["id"]
    body = {"data": {"price": 150, "count": 1}, "name": "Test object"}
    patch_update_object_fix.patch_object(body, object_id)
    patch_update_object_fix.check_statuscode_is_200()
    patch_update_object_fix.check_object_id(object_id)
    patch_update_object_fix.check_price(body['data']['price'])
    patch_update_object_fix.check_count(body['data']['count'])
    patch_update_object_fix.check_name(body['name'])


@allure.feature('Delete_object')
@allure.story('CRUD')
@pytest.mark.pozitive
def test_delete_object(create_test_object, delete_object_fix, get_object_fix):
    object_id = create_test_object["id"]
    delete_object_fix.delete_object(object_id)
    delete_object_fix.check_statuscode_is_200()
    get_object_fix.get_object(object_id)
    get_object_fix.check_statuscode_is_404()


@allure.feature('Get_object')
@allure.story('CRUD')
@pytest.mark.pozitive
def test_get_object(create_test_object, get_object_fix):
    object_id = create_test_object["id"]
    post_body = create_test_object
    get_object_fix.get_object(object_id)
    get_object_fix.check_statuscode_is_200()
    get_object_fix.check_name(post_body['name'])
    get_object_fix.check_price(post_body['data']['price'])
    get_object_fix.check_count(post_body['data']['count'])
