from fastapi import APIRouter
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str
    description: str | None = None
    complete: bool


Tasks = [
    Task(id=1, name="tarea 1", description="tarea 1 descripcion", complete=False),
    Task(id=2, name="tarea 2", description="descripcion tarea 2", complete=False)
]

router = APIRouter(prefix="/todo", tags=["todo"])


@router.get("/")
def get_task():
    return Tasks


@router.post("/")
def create_task(task: Task):
    Tasks.append(task)
    return task


@router.delete("/{id}")
def delete_task(id: int):
    for task in Tasks:
        if task.id == id:
            Tasks.remove(task)
            return task
