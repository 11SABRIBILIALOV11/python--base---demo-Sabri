from fastapi import FastAPI

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    return {"message":"pong 1234"}

