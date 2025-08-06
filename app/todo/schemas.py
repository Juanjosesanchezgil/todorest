from pydantic import BaseModel
from users.schemas import User


class Task(BaseModel):
    id: int
    name: str
    description: str | None = None
    complete: bool
    user: User
