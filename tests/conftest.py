import pytest
import allure
from endpoints.create_user import CreateObject
from endpoints.delete_user import DeleteObject


@allure.feature("Conftest Create and Delete user")
@pytest.fixture()
def user_id():
    new_user = CreateObject()
    delete_user = DeleteObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2025,
            "price": 2354.12,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    with allure.step("Create user"):
        new_user.create_object(payload)
    yield new_user.response_json['id']
    with allure.step("Delete user"):
        delete_user.delete_object(new_user.response_json['id'])
