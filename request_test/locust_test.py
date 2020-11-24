from locust import HttpUser, task, between


class WebUser(HttpUser):
    wait_time = between(5, 10)
    host = 'http://192.168.0.251:8002'

    @task
    def food(self):
        self.client.get('/v2/index_entry')

    def on_start(self):
        self.client.post('/admin/login', {'user_name': 'admin', 'password': '123456'})
