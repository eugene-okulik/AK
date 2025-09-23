from locust import HttpUser, task


class GetAllObject(HttpUser):
    headers = {'Content-Type': 'application/json'}

    @task
    def get_all_object(self):
        self.client.get("/object", headers=self.headers)


class CreateObject(HttpUser):
    headers = {'Content-Type': 'application/json'}
    body = {"data": {"price": 450, "count": 3}, "id": 1, "name": "Test object_3"}

    @task
    def create_object(self):
        self.client.post("/object", json=self.body, headers=self.headers)


class PutObject(HttpUser):
    object_id = None
    headers = {'Content-Type': 'application/json'}
    body = {"data": {"price": 450, "count": 3}, "id": 1, "name": "Test object_3"}

    def on_start(self):
        response = self.client.post("/object", json=self.body, headers=self.headers)
        self.object_id = response.json()['id']

    @task
    def update_post(self):
        put_body = {"data": {"price": 500, "count": 5}, "name": "Updated object"}
        self.client.put(f"/object/{self.object_id}", json=put_body, headers=self.headers)
