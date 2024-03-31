
# from sqlmodel import SQLModel
# from class1 import settings

# sqlmodel
# psycopg
# class ToDo









from fastapi import FastAPI
app:FastAPI = FastAPI()

@app.get('/cites')
def read_root():
    return {'cites':['lahore','sialkot','karachi']}

@app.get('/')
def read_rootcity():
     return {'city':'lahore'}

