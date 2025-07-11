import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"


def get_jwt_token(username, password):
    """Helper to get a JWT token for a user."""
    resp = requests.post(
        f"{BASE_URL}/login",
        json={"username": username, "password": password},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    return data["access_token"]


def test_basic_auth_no_credentials():
    resp = requests.get(f"{BASE_URL}/basic-protected")
    assert resp.status_code == 401


@pytest.mark.parametrize("username,password", [
    ("user1", "password"),
    ("admin1", "password"),
])
def test_basic_auth_valid_credentials(username, password):
    resp = requests.get(f"{BASE_URL}/basic-protected", auth=(username, password))
    assert resp.status_code == 200
    assert resp.text == "Basic Auth: Access Granted"


def test_basic_auth_invalid_credentials():
    resp = requests.get(f"{BASE_URL}/basic-protected", auth=("user1", "wrongpass"))
    assert resp.status_code == 401


@pytest.mark.parametrize("username,password", [
    ("user1", "password"),
    ("admin1", "password"),
])
def test_jwt_auth_valid_credentials(username, password):
    resp = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_jwt_auth_invalid_credentials():
    resp = requests.post(f"{BASE_URL}/login", json={"username": "user1", "password": "wrong"})
    assert resp.status_code == 401
    assert "error" in resp.json()


def test_jwt_protected_without_token():
    resp = requests.get(f"{BASE_URL}/jwt-protected")
    assert resp.status_code == 401


def test_jwt_protected_with_valid_token():
    token = get_jwt_token("user1", "password")
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    assert resp.status_code == 200
    assert resp.text == "JWT Auth: Access Granted"


def test_jwt_protected_with_invalid_token():
    headers = {"Authorization": "Bearer invalidtoken"}
    resp = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    assert resp.status_code == 401


def test_admin_without_token():
    resp = requests.get(f"{BASE_URL}/admin-only")
    assert resp.status_code == 401


def test_admin_with_wrong_token():
    # user1 is not admin
    token = get_jwt_token("user1", "password")
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/admin-only", headers=headers)
    assert resp.status_code == 403
    assert resp.json().get("error") == "Admin access required"


def test_admin_with_valid_token():
    # admin1 is admin
    token = get_jwt_token("admin1", "password")
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/admin-only", headers=headers)
    assert resp.status_code == 200
    assert resp.text == "Admin Access: Granted"