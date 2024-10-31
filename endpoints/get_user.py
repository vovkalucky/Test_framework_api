import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):
    response = None
    response_json = None
    endpoint = "/objects"

    @allure.story("Get object")
    def get_object(self, user_id):
        #self.response = requests.get(f"https://api.restful-api.dev/objects/{user_id}")
        self.response = requests.get(self.base_url + self.endpoint + f"/{user_id}")
        self.response_json = self.response.json()