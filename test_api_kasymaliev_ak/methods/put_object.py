import allure
import requests


from test_api_kasymaliev_ak.methods.master_endpoint import MasterMetod


class PutObject(MasterMetod):
    @allure.step('Put a object')
    def put_object(self, body, object_id):
        self.response = requests.put(f"{self.url}/{object_id}", json=body, headers=self.headers)
        self.json = self.response.json()
        return self.response
