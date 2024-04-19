from fastapi import APIRouter
from typing import Annotated
from pydantic import Field, BaseModel
router = APIRouter()


class Eduction(BaseModel):
    Bs: str = Field(default='math')


@router.post('/bodyfield')
async def bodyfield(educ: Eduction):
    return {"bodyfield": educ}
