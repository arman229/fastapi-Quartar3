# Step 1: import FastAPI
from fastapi import FastAPI, Query,Path,Body
from typing import Annotated,Union,Any
import uvicorn
from enum import Enum
from pydantic import BaseModel

# from tutorialfastapi.models import Language
# Step 2: create a FastAPI "instance"
app: FastAPI = FastAPI(title='This is the tutorial of fastapi documentation')


# Step 3: create a path operation
@app.get('/email')
# A "decorator" takes the function below and does something with it.
async def read_root(email: str) -> dict[str, str]:
    return {"message": f"Hello World {email}"}
 
@app.get("/itemhidden/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results 
@app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] =' ...'):
    # Query parameter list / multiple values
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            alias='item-querys' ,
            deprecated=True,
            
        ),
    ] = None,
):
    results:dict[str,list[dict[str,str]]|list[str]] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

 
@app.get('/')
# A "decorator" takes the function below and does something with it.
async def read_roots( ) -> dict[str, str]:
    return {"message": f"Hello World"}

@app.get('/book_number/{book_id}')
async def read_book_id(book_id: int ) -> dict[str, int]:
    return {"book_id": book_id}
@app.get("/items/{item_id}")
async def read_item(item_id: int ):
    return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item to get")):
    return {"item_id": item_id}

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
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.put("/items/{body_id}")
async def body_idfun(body_id: int,item:Item):
    result= {"body_id": body_id}
    return result

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
if __name__ == '__main__':
    main()
