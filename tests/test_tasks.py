from fastapi.testclient import TestClient
from app.main import app, tasks

client = TestClient(app)


def setup_function():
    tasks.clear()


def test_get_tasks_returns_empty_list():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_post_tasks_creates_task():
    response = client.post("/tasks", json={"title": "Finish assignment"})

    assert response.status_code == 201
    assert response.json()["title"] == "Finish assignment"