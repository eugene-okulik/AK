import allure
import requests


from test_api_kasymaliev_ak.methods.master_endpoint import MasterMetod


class CreateObject(MasterMetod):
    @allure.step('Create a object')
    def post_object(self, body):
        self.response = requests.post(self.url, json=body, headers=self.headers)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return self.response, self.json
