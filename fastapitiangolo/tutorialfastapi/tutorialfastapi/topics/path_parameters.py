from fastapi import APIRouter
from typing import Annotated
from tutorialfastapi.models import User, Item, Language


router = APIRouter()


@router.get('/PathParameterbook/{book_id}')
async def PathParameterbookid(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


@router.get("/PathParameteritem/{item_id}")
async def PathParameteritemid(item_id):
    return {"item_id": item_id}


@router.put("/PathParameteritem/{user_id}")
async def PathParameteruserid(user_id: int, item: Item):
    result = {"user_id": user_id}
    return result


@router.get('/PathParameterlanguage/{language}')
async def PathParameterlanguage(language: Language) -> dict[str, str]:
    return {"Declare a path parameters with types": language}


# http://127.0.0.1:8000/PathParameterfile/home/johndoe/index.html
# this is Path parameters containing paths  "home/johndoe/index.html"
@router.get("/PathParameterfile/{file_path:path}")
async def PathParameterfile(file_path: str):
    return {"file_path": file_path}
