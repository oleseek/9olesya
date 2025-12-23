import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestAPI:
    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200
    
    def test_response_json(self):
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()
        assert 'id' in data
        assert 'name' in data
    
    def test_simple(self):
        assert 1 + 1 == 2
