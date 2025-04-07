from fastapi import status
from fastapi.testclient import TestClient

from fastapi_todolist.app import app


def test_read_root():
    client = TestClient(app)
    response = client.get('/')
    expected_status = status.HTTP_200_OK
    assert response.status_code == expected_status
    assert response.json() == {'message': 'Hello World'}
