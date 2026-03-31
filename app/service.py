from fastapi import HTTPException
from app.storage import get_all_tasks, add_task, get_task_by_id


def list_tasks():
    return get_all_tasks()


def create_task(title: str):
    new_task = {
        "id": len(get_all_tasks()) + 1,
        "title": title,
        "status": "pending",
    }
    add_task(new_task)
    return new_task


def complete_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task["status"] = "completed"
    return task