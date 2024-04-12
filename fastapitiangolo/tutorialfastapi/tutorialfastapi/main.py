# Step 1: import FastAPI
from fastapi import FastAPI
import uvicorn
from enum import Enum

# from tutorialfastapi.models import Language
# Step 2: create a FastAPI "instance"
app: FastAPI = FastAPI(title='This is the tutorial of fastapi documentation')


# Step 3: create a path operation
@app.get('/')
# A "decorator" takes the function below and does something with it.
async def read_root(email: str) -> dict[str, str]:
    
    return {"message": f"Hello World {email}"}


@app.get('/book_number/{book_id}')
async def read_book_id(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


class Language(str, Enum):
    urdu = 'URDU'
    punjabi = 'PUNJABI'
    hindi = 'HINDI'
    english = 'ENGLISH'


@app.get('/language/{language}')
async def read_language(language: Language) -> dict[str, str]:
    return {"language": language}


# http://127.0.0.1:8000/files//home/johndoe/index.html
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == '__main__':
    main()
