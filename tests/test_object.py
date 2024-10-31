import allure
import pytest

from endpoints.create_user import CreateObject
from endpoints.get_user import GetObject
from endpoints.update_user import UpdateObject
from endpoints.delete_user import DeleteObject
from data.data import generate_data
from data.data import payload_data, payload_data_negative

#class Test_CRUD:


@allure.feature("Create new user [POSITIVE CASES]")
@pytest.mark.parametrize('data', payload_data)
def test_add_user(data):
    new_user = CreateObject()
    new_user.create_object(data)
    new_user.check_status(200)
    new_user.check_field(data["name"], "name")


@allure.feature("Create new user [NEGATIVE CASES]")
@pytest.mark.parametrize('data', payload_data_negative)
def test_add_user(data):
    new_user = CreateObject()
    new_user.create_object(data)
    new_user.check_status(200)
    new_user.check_field(data["name"], "name")


@allure.feature("Read data of user")
def test_get_user(user_id):
    user = GetObject()
    user.get_object(user_id)
    user.check_status(200)
    user.check_field(user_id, "id")


@allure.feature("Update data of user")
def test_update_user(user_id):
    user = UpdateObject()
    generate_object = generate_data()
    user.update_object(user_id, generate_object)
    user.check_status(200)


@allure.feature("Delete user")
def test_delete_user(user_id):
    user = DeleteObject()
    user.delete_object(user_id)
    user.check_status(200)
    user = GetObject()
    user.get_object(user_id)
    user.check_status(404)


