from fastapi import APIRouter
from .model import User
from database import SessionDep


users = [
    User(id=1, name="Juan", surname="Sanchez", age=41),
    User(id=2, name="Manuel", surname="Lopez", age=34)
]

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users():
    return (users)


@router.get("/{id}")
def get_user(id: int):
    for user in users:
        if user.id == id:
            return user


@router.post("/", response_model=User)
def create_user(user: User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
