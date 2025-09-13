import pytest
import requests


@pytest.fixture(scope='session')
def session_function():
    print('Start testing"')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def before_and_after_function():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def object_for_test():
    body = {
        "data": {"price": 350,
                 "count": 1},
        "id": 2,
        "name": "object for testing"
    }
    headers = {'Content-Type': 'application/json'}
    post_response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    print("Тело объекта: ", post_response.json())
    object_id = post_response.json()['id']
    yield object_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}", headers=headers)


@pytest.mark.parametrize('body', [{"data": {"price": 150, "count": 1}, "id": 1, "name": "Test object"},
                                  {"data": {"price": 300, "count": 2}, "id": 1, "name": "Test object_2"},
                                  {"data": {"price": 450, "count": 3}, "id": 1, "name": "Test object_3"}])
@pytest.mark.critical
def test_post_object(body, session_function, before_and_after_function):  # Проверка POST
    headers = {'Content-Type': 'application/json'}
    post_response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    assert post_response.status_code == 200, "Ошибка при создании объекта"
    assert post_response.json()['data']['price'] == body["data"]["price"], "Ошибка при сохранении поля 'price'"
    assert post_response.json()['data']['count'] == body["data"]["count"], "Ошибка при сохранении поля 'count'"
    assert post_response.json()['name'] == body["name"], "Ошибка при сохранении поля 'name'"
    delete_post = requests.delete(f"http://objapi.course.qa-practice.com/object/{post_response.json()['id']}",
                                  headers=headers)
    assert delete_post.status_code == 200, "Ошибка при удалении объекта"


@pytest.mark.medium
def test_put_object(object_for_test, before_and_after_function):  # Проверка PUT
    body = {
        "data": {"price": 300,
                 "count": 2},
        "id": object_for_test,
        "name": "Test object version 1"
    }
    headers = {'Content-Type': 'application/json'}
    put_response = requests.put(f"http://objapi.course.qa-practice.com/object/{object_for_test}", json=body,
                                headers=headers)
    assert put_response.status_code == 200, "Ошибка при изменении объекта"
    assert put_response.json()['data']['price'] == 300, "Ошибка при изменении поля 'price'"
    assert put_response.json()['data']['count'] == 2, "Ошибка при изменении поля 'count'"
    assert put_response.json()['name'] == 'Test object version 1', "Ошибка при изменении поля 'name'"
    assert put_response.json()['id'] == str(object_for_test), "Ошибка при изменении поля 'id'"


def test_patch_object(object_for_test, before_and_after_function):  # Проверка PATCH
    body = {
        "data": {"price": 250,
                 },
        "name": "Test object version 2"
    }
    headers = {'Content-Type': 'application/json'}
    patch_response = requests.patch(f"http://objapi.course.qa-practice.com/object/{object_for_test}", json=body,
                                    headers=headers)
    assert patch_response.status_code == 200, "Ошибка при изменении объекта"
    assert patch_response.json()['data']['price'] == 250, " Ошибка при изменении поля 'price'"
    # assert patch_response.json()['data']['count'] == 1, "Невалидное значение в поле 'count'"
    assert patch_response.json()['name'] == 'Test object version 2', "Ошибка при изменении поля 'name'"


def test_delete_object(object_for_test, before_and_after_function, session_function):
    headers = {'Content-Type': 'application/json'}
    delete_response = requests.delete(f"http://objapi.course.qa-practice.com/object/{object_for_test}",
                                      headers=headers)
    assert delete_response.status_code == 200, "Ошибка при удалении объекта"
    check_response = requests.get(f"http://objapi.course.qa-practice.com/object/{object_for_test}",
                                  headers=headers)
    if check_response.status_code != 404:
        raise Exception("Объект не удалён!")
