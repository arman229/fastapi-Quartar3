
 
from fastapi import APIRouter

router = APIRouter()


@router.get('/firststep')
def get_firststep():
    return {"message": "Hello world firststep"}
