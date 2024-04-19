from fastapi import APIRouter,Path
from typing import Annotated

router = APIRouter()

@router.get("/ppvalidation/{item_id}")
async def read_items( item_id: Annotated[int|str|None, Path(title="The ID of the item to get",ge=0, le=300)] ):
    return {"item_id": item_id}
 
 
