from fastapi import FastAPI
from todo.router import router as todo
from users.router import router as users


app = FastAPI()
app.include_router(todo)
app.include_router(users)


@app.get("/")
def root():
    return {"msg": "Hello world"}
