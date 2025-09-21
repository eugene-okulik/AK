import requests


from test_api_kasymaliev_ak.methods.master_endpoint import MasterMetod


class GetObject(MasterMetod):
    def get_object(self, object_id):
        self.response = requests.get(url=f"{self.url}/{object_id}")
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = None
        return self.response, self.json
