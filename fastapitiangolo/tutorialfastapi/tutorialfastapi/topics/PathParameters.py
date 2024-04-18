from fastapi import APIRouter

router = APIRouter()


@router.get('/PathParameterbook/{book_id}')
async def PathParameterbookid(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


@router.get("/PathParameteritem/{item_id}")
async def PathParameteritemid(item_id: int):
    return {"item_id": item_id}
