from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []


class TaskCreate(BaseModel):
    title: str


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title
    }
    tasks.append(new_task)
    return new_task