from fastapi import APIRouter, Header, Response
from typing import Annotated

router = APIRouter()


@router.get("/headerparmeters/")
async def read_items(response: Response, myName: Annotated[str | None, Header()] = None):
    response.set_cookie(key="user_quer", value=myName)
    return {"User-Agent": myName}
