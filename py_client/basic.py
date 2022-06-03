import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #"http://localhost:8000/"

get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "abcd1234"}) # HTTP Request
# print(get_response.headers)
# print(get_response.text) # print source code
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json())
# print(get_response.status_code)