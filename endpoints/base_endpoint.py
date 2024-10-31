import allure


class BaseEndpoint:
    response = None
    response_json = None
    base_url = "https://api.restful-api.dev"

    @allure.story("Check status")
    def check_status(self, status):
        assert self.response.status_code == status

    @allure.story("Check field")
    def check_field(self, request, response_field):
        assert self.response_json[f"{response_field}"] == request #field ="Apple MacBook Pro 16"