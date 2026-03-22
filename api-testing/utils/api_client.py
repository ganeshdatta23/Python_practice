import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    return requests.get(f"{BASE_URL}/users")

def create_post(payload):
    return requests.post(f"{BASE_URL}/posts", json=payload)