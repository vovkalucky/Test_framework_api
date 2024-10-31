import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    response = None
    response_json = None
    endpoint = "/objects"

    @allure.story("Delete object")
    def delete_object(self, user_id):
        #self.response = requests.delete(f"https://api.restful-api.dev/objects/{user_id}")
        self.response = requests.delete(self.base_url + self.endpoint + f"/{user_id}")
        self.response_json = self.response.json()