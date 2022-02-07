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
for method_name in methods:
    print(method_name)
    for parameter_name in parameters:
        if method_name != 'get':
            response4 = requests.request(method_name, url, data=parameter_name)
        else:
            response4 = requests.request(method_name, url, params=parameter_name)
        print(f"При вызове метода {method_name} c параметром method={parameter_name['method']} получаем ответ: {response4.text}")
