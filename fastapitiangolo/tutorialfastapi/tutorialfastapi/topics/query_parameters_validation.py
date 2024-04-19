from fastapi import APIRouter, Query
from typing import Annotated

router = APIRouter()


@router.get('/qpvalidation')
def get_validation(query : Annotated[
       list[str],
        Query(...,
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=30,
            alias='item-querys',
           deprecated=True,
            include_in_schema=False
             

        ),
] = []):
    
    return {'query': query}

@router.get("/itemhidden/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


 