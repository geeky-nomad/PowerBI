from fastapi import status
from fastapi.testclient import TestClient

from .test_main import app


client = TestClient(app)


class TestUserMe:

    def __init__(self):
        self.token = token_db.get('access_token', None)
        self.url = "/users/me"
        self.invalid_token = "54e517d7c9c64208991c3dce928a5b6e"

    def test_user_me_success(self):
        response = client.post(self.url, headers=self.token)
        assert response.status_code == status.HTTP_200_OK
        expected_response = {
            "username": "johndoe",
            "firstname": "john",
            "lastname": "doe",
            "email": "johndoe@mailinator.com",
            "created_at": "2022-11-25 01:26:03.478039"
        }
        assert response == expected_response

    def test_user_me_failed(self):
        response = client.post(self.url, headers=self.invalid_token)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        expected_response = {"detail": "Invalid token"}
        assert response == expected_response


class TestUserAll:

    def __init__(self):
        self.token = token_db.get('access_token', None)
        self.url = "/users/all"
        self.invalid_token = "54e517d7c9c64208991c3dce928a5b6e]"

    def test_user_all_success(self):
        response = client.post(self.url, headers=self.token)
        assert response.status_code == status.HTTP_200_OK
        expected_response = [
            {
                "username": "johndoe",
                "firstname": "john",
                "lastname": "doe",
                "email": "johndoe@mailinator.com",
                "created_at": "2022-11-25 01:26:03.478039"
            },
            {
                "username": "aliceblue",
                "firstname": "Alice",
                "lastname": "Blue",
                "email": "alice@mailinator.com",
                "created_at": "2022-11-25 01:36:03.478039"
            }
        ]
        assert response == expected_response

    def test_user_all_failed(self):
        response = client.post(self.url, headers=self.invalid_token)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        expected_response = {"detail": "Invalid token"}
        assert response == expected_response
