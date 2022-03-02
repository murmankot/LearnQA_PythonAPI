from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("Delete user cases")
class TestUserDelete(BaseCase):
    def test_delete_user_with_id_2(self):
        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = MyRequests.delete(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
            )

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_error_by_text(response2,
                                        'Please, do not delete test users with ID 1, 2, 3, 4 or 5.',
                                        f"Unexpected response content {response2.content}")

    def test_delete_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        # CHECK DELETE

        response4 = MyRequests.get(f"/user/{user_id}")

        Assertions.assert_code_status(response4, 404)
        Assertions.assert_error_by_text(response4,
                                        'User not found',
                                        f"Unexpected response content {response4.content}")

    def test_delete_user_by_another_auth_user(self):
        # REGISTER1 FOR DELETE
        register_data1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        user_id_delete = self.get_json_value(response1, "id")
        username = register_data1["username"]

        # REGISTER2 FOR AUTH
        register_data2 = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email = register_data2['email']
        password = register_data2['password']
        user_id_auth = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response3 = MyRequests.post("/user/login", data=login_data)

        auth_sid_auth = self.get_cookie(response3, "auth_sid")
        token_auth = self.get_header(response3, "x-csrf-token")

        # DELETE
        response4 = MyRequests.delete(
            f"/user/{user_id_delete}",
            headers={"x-csrf-token": token_auth},
            cookies={"auth_sid": auth_sid_auth}
        )

        Assertions.assert_code_status(response4, 200)

        # GET
        response5 = MyRequests.get(f"/user/{user_id_delete}")

        Assertions.assert_code_status(response5, 200)
        Assertions.assert_json_has_key(response5, "username")
