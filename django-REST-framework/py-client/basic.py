import requests
 
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

data = {"title": "Abc123", "price": 12}

response = requests.post(endpoint, json=data)

print(response.text)
# print(response.status_code)

print(response.json)