

from fastapi import APIRouter

router = APIRouter()

# A "decorator" takes the function below and does something with it(call automatically the below function).


@router.get('/firststep')
def get_firststep():
    return {"message": "Hello world firststep"}
