from fastapi import FastAPI
from database import create_db_and_tables
from todo.router import router as todo
from users.router import router as users


app = FastAPI()

create_db_and_tables()

app.include_router(todo)
app.include_router(users)


@app.get("/")
def root():
    return {"msg": "Hello world"}
