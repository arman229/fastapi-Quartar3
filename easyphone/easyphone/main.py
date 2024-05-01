from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def helloworld():
  return {"message": " easy phone Hello World"}

@app.get('/easyphone')
def Easyphone():
  return {"EasyPhone": " This is Easy Phone routes"}