import requests


class Test11:
    def test_cookie_and_fix(self):
        response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        cookies = response.cookies.get_dict()
        print(cookies)
        assert "HomeWork" in response.cookies, "There is no 'HomeWork' cookie in the response"
        assert response.cookies.get("HomeWork") == 'hw_value'
