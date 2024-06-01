from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def hello():
    return{ "message ":"hello World"}
@app.get("/name")
def name():
   return{ "Name ":"My name is Arman ashraf "}    
@app.get("/docker")
def docker():
    return{ "Topic ":"Docker"}