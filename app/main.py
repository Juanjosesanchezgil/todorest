from fastapi import FastAPI
from todo.router import router as todo


app = FastAPI()
app.include_router(todo)


@app.get("/")
def root():
    return {"msg": "Hello world"}
