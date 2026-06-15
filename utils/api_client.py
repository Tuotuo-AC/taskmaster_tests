# 封装HTTP请求
import requests
from config import BASE_URL, TIMEOUT

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url, params=params, timeout=self.timeout)

    def post(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, json=json, timeout=self.timeout)

    def put(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        return requests.put(url, json=json, timeout=self.timeout)

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        return requests.delete(url, timeout=self.timeout)