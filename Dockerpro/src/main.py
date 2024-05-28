from fastapi import FastAPI

apps = FastAPI()
@apps.get("/")
def hello():
    return{ "message ":"hello World"}