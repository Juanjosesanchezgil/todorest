from fastapi import APIRouter
from .schemas import Task


tasks = [
    Task(id=1, name="tarea 1", description="tarea 1 descripcion",
         complete=False, user=(id=1, name="Juan", surname="Sanchez", age=41)),
    Task(id=2, name="tarea 2", description="descripcion tarea 2",
         complete=False)
]

router = APIRouter(prefix="/todo", tags=["todo"])


@router.get("/")
def get_task():
    return tasks


@router.post("/")
def create_task(task: Task):
    tasks.append(task)
    return task


@router.put("/{id}")
async def update_task(id: int, task_update: Task):
    for i, task in enumerate(tasks):
        if task.id == id:
            tasks[i] = task_update
            return task_update


@router.delete("/{id}")
def delete_task(id: int):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return task
