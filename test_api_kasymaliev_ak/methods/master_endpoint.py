import allure


class MasterMetod:
    url = 'http://objapi.course.qa-practice.com/object'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None

    @allure.step('Check status code')
    def check_statuscode_is_200(self):
        assert self.response.status_code == 200, "Ошибка при создании объекта"

    @allure.step('Check price')
    def check_price(self, price):
        assert self.json['data']['price'] == price, (f"Ожидали price = {price},"
                                                     f" получили {self.json['data']['price']}")

    @allure.step('Check count')
    def check_count(self, count):
        assert self.json['data']['count'] == count, (f"Ожидали count = {count},"
                                                     f" получили {self.json['data']['price']}")

    @allure.step('Check name')
    def check_name(self, name):
        assert self.json['name'] == name, f"Ожидали name = {name}, получили {self.json['name']}"

    @allure.step('Check status code 400')
    def check_statuscode_is_400(self):
        assert self.response.status_code == 400, "Объект не создан"

    @allure.step('Check object id')
    def check_object_id(self, object_id):
        assert str(self.json['id']) == str(object_id), (f"Ожидали object_id = {object_id},"
                                                        f" получили {self.json['id']}")

    @allure.step('Check object not found')
    def check_statuscode_is_404(self):
        assert self.response.status_code == 404, "Объект не найден"
