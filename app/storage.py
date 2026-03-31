tasks = []


def get_all_tasks():
    return tasks


def add_task(task):
    tasks.append(task)


def get_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None