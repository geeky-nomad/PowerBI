from fastapi import Request
from fastapi import status
from fastapi.testclient import TestClient

from .test_main import app


client = TestClient(app)


def test_login():
    response = client.post(
        "/login", json={"username": "johndoe", "password": "hello@123"})
    assert response.status_code == 200


def test_login_failed():
    response = client.post(
        "/login", json={"username": "prakash", "password": "hello@123"})
    assert response.status_code == 401


def test_logout():
    response = client.post("/logout", json={"token": "faslkfjlskf8989lkjsad2"})
    assert response.status_code == 200


def test_logout_failed():
    response = client.post("/logout", json={"token": "faslkfjlskf8989lkjsad3"})
    assert response.status_code == 401
