import requests
 
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


response = requests.get(endpoint, params={"abc": 123}, json={"query": "test"})

print(response.text)
# print(response.status_code)

print(response.json)