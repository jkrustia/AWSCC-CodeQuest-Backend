import requests
import json

api_url = "https://jsonplaceholder.typicode.com/posts"

headers = {"user-agent": "MyApp/1.0"}

response = requests.get(api_url, headers=headers)

print("Response Status Code: ", response.status_code)
print("Response Headers: ")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print("Response Content: ", response.text)

data = {
    "title": "2024", 
    "body": "Happy New Year!"   
    }

post_response = requests.post(api_url, json=data)

print("POST Response: ", post_response.status_code)
print(post_response.text)