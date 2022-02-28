from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from random import choice
from string import ascii_letters
import pytest


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email=email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    def test_create_user_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email=email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content {response.content}"

    exclude_params2 = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]

    @pytest.mark.parametrize('condition', exclude_params2)
    def test_create_no_fields(self, condition):
        response = self.send_request_without_param(key=condition)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_error_by_text(
            response,
            f'The following required params are missed: {condition}',
            f"Unexpected response content {response.content}"
        )

    def test_create_user_short_username(self):
        username = (''.join(choice(ascii_letters) for i in range(1)))
        data = self.prepare_registration_data(username=username)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", \
            f"Unexpected response content {response.content}"

    def test_create_user_long_firstname(self):
        firstname = (''.join(choice(ascii_letters) for i in range(251)))
        data = self.prepare_registration_data(firstname=firstname)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long", \
            f"Unexpected response content {response.content}"
