from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend_authportal.database import engine

from backend_authportal.model import NewUsers


def create_tables():
    NewUsers.metadata.create_all(engine)
     
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("This statement will executes before the Creating tables....")
    create_tables()
    yield  
     
 