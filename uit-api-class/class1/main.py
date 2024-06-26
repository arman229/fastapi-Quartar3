
# from sqlmodel import SQLModel
# from class1 import settings

# sqlmodel
# psycopg
# class ToDo

import uvicorn

from typing import Dict
from fastapi import FastAPI
app: FastAPI = FastAPI()


@app.get('/')
def print_name():
    return {'name': 'My name is Arman'}


@app.get('/cites')
def read_root():
    return {'cites': ['lahore', 'sialkot', 'karachi']}
# http://127.0.0.1:8000/?query=lahore


@app.get('/', response_model=Dict[str, str])
def read_rootcity(query: str):
    return {'city': 'lahore', 'queryparmeters': query}


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
