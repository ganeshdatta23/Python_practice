import json
import pytest
import allure
from requests.models import Response

from utils.api_client import BASE_URL, get_users, create_post


def _fake_response(status_code: int, payload: dict | list) -> Response:
    """Build a minimal Response object with the given payload."""
    resp = Response()
    resp.status_code = status_code
    resp._content = json.dumps(payload).encode()
    return resp


@allure.feature("Users API")
@allure.story("Get Users List")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_users(monkeypatch):
    sample_users = [{"id": 1, "name": "Test User"}]

    def fake_get(url: str):
        assert url == f"{BASE_URL}/users"
        return _fake_response(200, sample_users)

    monkeypatch.setattr("utils.api_client.requests.get", fake_get)

    with allure.step("Send GET request to fetch users"):
        response = get_users()

    with allure.step("Validate status code"):
        assert response.status_code == 200

    with allure.step("Validate response structure"):
        data = response.json()
        assert isinstance(data, list)
        assert "id" in data[0]
        assert "name" in data[0]


@allure.feature("Posts API")
@allure.story("Create Post")
@allure.severity(allure.severity_level.NORMAL)
def test_create_post(monkeypatch):
    payload = {
        "title": "Ganesh Test",
        "body": "Learning API Automation",
        "userId": 1
    }

    def fake_post(url: str, json: dict):
        assert url == f"{BASE_URL}/posts"
        # mimic API creating an id
        return _fake_response(201, {**json, "id": 101})

    monkeypatch.setattr("utils.api_client.requests.post", fake_post)

    with allure.step("Send POST request"):
        response = create_post(payload)

    with allure.step("Validate status code"):
        assert response.status_code == 201

    with allure.step("Validate response data"):
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["userId"] == payload["userId"]
