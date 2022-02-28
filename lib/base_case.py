import json.decoder

from requests import Response
from datetime import datetime

from random import choice
from string import ascii_letters
from string import digits
from lib.my_requests import MyRequests


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find cookie with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self,  username=None, firstname=None, lastname=None, email=None, password=None):
        if username is None:
            username = (''.join(choice(ascii_letters) for i in range(9)))
        if firstname is None:
            firstname = (''.join(choice(ascii_letters) for i in range(10)))
        if lastname is None:
            lastname = (''.join(choice(ascii_letters) for i in range(12)))
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        if password is None:
            password = (''.join(choice(digits) for i in range(10)))
        return {
            'username': username,
            'firstName': firstname,
            'lastName': lastname,
            'email': email,
            'password': password
        }

    def send_request_without_param(self, key, data=None):
        if data is None:
            data = self.prepare_registration_data()
        try:
            del data[key]
        except KeyError:
            raise Exception(f"Key {key} does not exist in {data}")
        response = MyRequests.post("/user/", data=data)
        return response

