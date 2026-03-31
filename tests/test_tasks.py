from fastapi.testclient import TestClient
from app.main import app
from app.storage import tasks

from fastapi.testclient import TestClient
from app.main import app
from app.storage import tasks

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
    assert response.json() == {
        "id": 1,
        "title": "Finish assignment",
        "status": "pending",
    }


def test_post_tasks_rejects_missing_title():
    response = client.post("/tasks", json={})

    assert response.status_code == 422


def test_post_tasks_rejects_blank_title():
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code == 422


def test_patch_tasks_marks_task_as_completed():
    create_response = client.post("/tasks", json={"title": "Finish assignment"})
    task_id = create_response.json()["id"]

    response = client.patch(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": task_id,
        "title": "Finish assignment",
        "status": "completed",
    }


def test_patch_tasks_returns_404_for_missing_task():
    response = client.patch("/tasks/999")

    assert response.status_code == 404