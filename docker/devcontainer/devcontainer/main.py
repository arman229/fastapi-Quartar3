from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "new Dev container"}
@app.get("/devcontainer")
def read_root():
    return {"Hello": "new changing from Dev container"}