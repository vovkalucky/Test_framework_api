import requests
from endpoints.base_endpoint import BaseEndpoint
import allure


class CreateObject(BaseEndpoint):
    response = None
    response_json = None
    endpoint = "/objects"

    @allure.story("Create object")
    def create_object(self, payload):
        self.response = requests.post(self.base_url + self.endpoint, json=payload)
        self.response_json = self.response.json()