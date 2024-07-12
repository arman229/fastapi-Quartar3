from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend_authportal.database import engine 
from sqlmodel import SQLModel

def create_tables():
    SQLModel.metadata.create_all(engine)
     
@asynccontextmanager
async def newlifespan(app: FastAPI):
    print("This statement will executes before the Creating tables....")
    create_tables()
    yield  
     
 