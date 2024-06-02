from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/devcontainer")
def read_root():
    return {"Hello": "Dev container"}