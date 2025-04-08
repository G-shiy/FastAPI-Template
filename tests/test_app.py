from fastapi import status
from fastapi.testclient import TestClient

from fastapi_todolist.app import app

client = TestClient(app)


def test_create_user():
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword",  # Enviado, mas não será retornado
        "is_active": True,
        "is_superuser": False,
    }

    expected_response = {
        "id": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "is_active": True,
        "is_superuser": False,
    }

    response = client.post("/users/", json=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == expected_response


def test_health_check():
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "healthy"}
