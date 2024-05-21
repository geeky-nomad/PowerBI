from fastapi import status
from fastapi.testclient import TestClient

from .test_main import app


client = TestClient(app)


class TestItem:

    def __init__(self):
        self.id = 1
        self.url = "/items/" + self.id
        self.token = token_db.get('access_token', None)

    def test_item(self):
        data = {
            "token": self.token,
            "item_id": self.id
        }

        response = client.post(self.url, headers=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        expected_response = {
            "detail": "Permission denied"
        }
        assert response == expected_response


class TestItemsAll:

    def __init__(self):
        self.id = 1
        self.url = "/items/" + self.id
        self.token = token_db.get('access_token', None)

    def test_items(self):
        data = {
            "token": self.token,
            "item_id": self.id
        }

        response = client.post(self.url, headers=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        expected_response = {
            "detail": "Permission denied"
        }
        assert response == expected_response
