import requests


def post_object():  # Проверка POST

    body = {
        "data": {"price": 150,
                 "count": 1},
        "id": 1,
        "name": "Test object"
    }
    headers = {'Content-Type': 'application/json'}
    post_response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    print("Тело созданного объекта: ", post_response.json())
    print("Статус код запроса: ", post_response.status_code)
    assert post_response.status_code == 200, "Ошибка при создании объекта"
    assert post_response.json()['data']['price'] == 150, "Ошибка при сохранении поля 'price'"
    assert post_response.json()['data']['count'] == 1, "Ошибка при сохранении поля 'count'"
    assert post_response.json()['name'] == 'Test object', "Ошибка при сохранении поля 'name'"


def object_for_test():
    body = {
        "data": {"price": 150,
                 "count": 1},
        "id": 2,
        "name": "Test object"
    }
    headers = {'Content-Type': 'application/json'}
    post_response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    print("Тело объекта: ", post_response.json())
    return post_response.json()['id']


def clear(object_id):
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


# Проверка PUT
def put_object():
    object_id = object_for_test()
    body = {
        "data": {"price": 300,
                 "count": 2},
        "id": object_id,
        "name": "Test object version 1"
    }
    headers = {'Content-Type': 'application/json'}
    put_response = requests.put(f"http://objapi.course.qa-practice.com/object/{object_id}", json=body,
                                headers=headers)
    print("Тело объекта при полном изменении: ", put_response.json())
    check_response = requests.get(f"http://objapi.course.qa-practice.com/object/{object_id}",
                                  headers=headers)
    print("Статус код запроса: ", check_response.status_code)
    assert put_response.status_code == 200, "Ошибка при изменении объекта"
    assert put_response.json()['data']['price'] == 300, "Ошибка при изменении поля 'price'"
    assert put_response.json()['data']['count'] == 2, "Ошибка при изменении поля 'count'"
    assert put_response.json()['name'] == 'Test object version 1', "Ошибка при изменении поля 'name'"
    assert put_response.json()['id'] == str(object_id), "Ошибка при изменении поля 'id'"
    clear(object_id)


def patch_object():  # Проверка PATCH
    object_id = object_for_test()
    body = {
        "data": {"price": 250,
                 },
        "name": "Test object version 2"
    }
    headers = {'Content-Type': 'application/json'}
    patch_response = requests.patch(f"http://objapi.course.qa-practice.com/object/{object_id}", json=body,
                                    headers=headers)
    check_response = requests.get(f"http://objapi.course.qa-practice.com/object/{object_id}",
                                  headers=headers)
    print('Проверка всего тела после изменения', check_response.json())
    print("Тело объекта при частичном: ", patch_response.json())
    assert patch_response.status_code == 200, "Ошибка при изменении объекта"
    assert patch_response.json()['data']['price'] == 250, " Ошибка при изменении поля 'price'"
    assert patch_response.json()['data']['count'] == 1, "Невалидное значение в поле 'count'"
    assert patch_response.json()['name'] == 'Test object version 2', "Ошибка при изменении поля 'name'"
    clear(object_id)


def delete_object():
    object_id = object_for_test()
    headers = {'Content-Type': 'application/json'}
    delete_response = requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}", headers=headers)
    print(delete_response.status_code)
    assert delete_response.status_code == 200, "Ошибка при удалении объекта"
    check_response = requests.get(f"http://objapi.course.qa-practice.com/object/{object_id}",
                                  headers=headers)
    if check_response.status_code != 404:
        raise Exception("Объект не удалён!")


post_object()
put_object()
patch_object()  # стирает count
delete_object()
