import requests

# 7.1 Call method without parameters
print('Задание 7.1')
response1 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response1.status_code, response1.text)

# 7.2 Call method with type HEAD
print('Задание 7.2')
response2 = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response2.status_code, response2.text)

# 7.3 Call method with correct parameter "method"
print('Задание 7.3')
payload3 = {"method": "DELETE"}
response3 = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data=payload3)
print(response3.status_code, response3.text)

# 7.4 Find all answer combinations
print('Задание 7.4')
parameters = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
methods = ['get', 'post', 'put', 'delete']
url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

# обход циклом со всеми сочетаниями методов и параметров
list_of_answers = []
for method_name in methods:
    for parameter_name in parameters:
        if method_name != 'get':
            response4 = requests.request(method_name, url, data=parameter_name)
            list_of_answers.append([method_name, parameter_name['method'], response4.text])
        else:
            response4 = requests.request(method_name, url, params=parameter_name)
            list_of_answers.append([method_name, parameter_name['method'], response4.text])

# проверка корректности ответов после обхода методов циклом
list_of_answers_new = []
for answer in list_of_answers:
    if answer[0].casefold() == answer[1].casefold():
        if answer[2] == '{"success":"!"}':
            list_of_answers_new.append([answer[0], answer[1], answer[2], "Ответ корректный"])
    else:
        if answer[2] == 'Wrong method provided':
            list_of_answers_new.append([answer[0], answer[1], answer[2], "Ответ корректный"])
        else:
            list_of_answers_new.append([answer[0], answer[1], answer[2], "Ответ некорректный"])

# поиск некорректных ответов и вывод, если они есть
for item in list_of_answers_new:
    if item[3] == 'Ответ некорректный':
        print('Метод compare_query_type отвечает некорректно при сочетании параметров:', item)
