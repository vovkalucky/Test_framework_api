import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):
    response = None
    response_json = None
    endpoint = "/objects"
    @allure.story("Update object")
    def update_object(self, user_id, payload):
        #self.response = requests.put(f"https://api.restful-api.dev/objects/{user_id}", json=payload)
        self.response = self.response = requests.put(self.base_url + self.endpoint + f"/{user_id}", json=payload)
        self.response_json = self.response.json()