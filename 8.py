import requests
import json
import time

# 8.1 Вызов метода без токена
print('Задание 8.1')

response1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
print(f'Вызов метода без токена. Получен ответ метода:', response1.text)

# вытаскиваем нужные значения в разных форматах
token = {"token": (json.loads(response1.text))['token']}
seconds = (json.loads(response1.text))['seconds']
token_for_print = (json.loads(response1.text))['token']

# 8.2 Вызов метода c токеном и проверка поля status.
print('Задание 8.2')

response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)
print(f'Вызов метода с токеном {token_for_print}. Получен ответ метода:', response2.text)

# проверка значения поля status.
if (json.loads(response2.text))['status'] == 'Job is NOT ready':
     print('Поле status корректно')
else:
     print('Поле status не корректно')

# 8.3 Ожидание нужного количества секунд перед вызовом метода
print('Задание 8.3')

print(f"Ждем пока задача {token_for_print} выполнится еще {seconds} секунд")
time.sleep(seconds+1)

# 8.4 Вызов метода и проверка наличия поля result. Для выполнения негативного теста закомментировать строку c time.sleep
print('Задание 8.4')

response3 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)
print(f'Вызов метода с токеном {token_for_print} после ожидания {seconds}. Получен ответ метода:', response3.text)

# проверка значения поля status
if (json.loads(response3.text))['status'] == 'Job is ready':
     print('Поле status корректно')
else:
     print('Поле status не корректно')

# проверка наличия поля result
try:
    print(f"Поле result присутствует. Значение поля:{(json.loads(response3.text))['result']}")
except KeyError:
    print('Поле result отсутствует')
