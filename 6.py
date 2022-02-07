import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)

list_of_redirects = response.history
number_of_redirects = len(list_of_redirects)
print(number_of_redirects)
print(response.url)
