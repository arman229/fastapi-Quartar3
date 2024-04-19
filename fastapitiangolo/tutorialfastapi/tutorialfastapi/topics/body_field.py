from fastapi import APIRouter
 
router = APIRouter()
@router.get('/bodyfield')
async def bodyfield():
    return {"bodyfield": "bodyfield"}


 
