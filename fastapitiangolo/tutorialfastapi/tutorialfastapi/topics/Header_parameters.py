from fastapi import APIRouter,Header
from typing import Annotated

router = APIRouter()

@router.get("/headerparmeters/")
async def read_items(custom_header: str = Header(None, convert_underscores=False)):
    return {"x_custom_header": custom_header}