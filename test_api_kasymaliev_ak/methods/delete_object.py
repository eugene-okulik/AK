import allure
import requests


from test_api_kasymaliev_ak.methods.master_endpoint import MasterMetod


class DeleteObject(MasterMetod):
    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.response = requests.delete(url=f"{self.url}/{object_id}", headers=self.headers)
        check_object = requests.get(url=f"{self.url}/{object_id}")
        return self.response, check_object
