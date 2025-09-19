import allure
import requests


from test_api_kasymaliev_ak.methods.master_endpoint import MasterMetod


class PatchObject(MasterMetod):
    @allure.step('Patch a object')
    def patch_object(self, body, object_id):
        self.response = requests.patch(f"{self.url}/{object_id}", json=body,
                                       headers=self.headers)
        self.json = self.response.json()
        return self.response
