from fastapi import FastAPI
from app.schemas import TaskCreate
from app.service import list_tasks, create_task, complete_task

app = FastAPI()


@app.get("/tasks")
def get_tasks():
    return list_tasks()


@app.post("/tasks", status_code=201)
def post_task(task: TaskCreate):
    return create_task(task.title)


@app.patch("/tasks/{task_id}")
def patch_task(task_id: int):
    return complete_task(task_id)