from locust import HttpUser, task, between
import os


class WebUser(HttpUser):
    wait_time = between(5, 10)
    host = 'http://192.168.0.251:8002'

    @task
    def food(self):
        self.client.get('/v2/index_entry')

    def on_start(self):
        self.client.post('/admin/login', {'user_name': 'admin', 'password': '123456'})


if __name__ == '__main__':
    os.system('locust -f locust_test.py --web-host=127.0.0.1')