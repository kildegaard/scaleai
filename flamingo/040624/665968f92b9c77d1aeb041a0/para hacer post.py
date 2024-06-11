import requests

url = "http://127.0.0.1:5000/register"
data = {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword",
}

response = requests.post(url, json=data)
print(response.json())
