from fastapi import APIRouter,Body
from pydantic import BaseModel
from typing import Annotated

router = APIRouter()

class Name(BaseModel):
    first_name: str
    last_name: str
    
class Email(BaseModel):
    email: str    

@router.get("/bmparameters/{item_id}")
async def bodymultipleitemid(item_id: int,name:Name,email:Email,exterbody:Annotated[int,Body( )]):
    result = {"item_id": item_id, "My Complete Name is ": f'{name.first_name}{name.last_name}', "email": email,'externalbody': exterbody}
    return result

@router.post("/bmparametersw/ ")
async def bodymultipleitemidw( exterbody:Annotated[Email,Body(embed=True)]):
    result = { 'externalbody': exterbody}
    return result
 