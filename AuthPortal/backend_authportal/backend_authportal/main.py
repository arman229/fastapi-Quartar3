from fastapi import FastAPI
import uvicorn
# from backend_authportal import settings
# from sqlmodel import create_engine, Session
# from backend_authportal import model
# from contextlib import asynccontextmanager
from backend_authportal import model
 

# @asynccontextmanager
# async def beforeStarting(app: FastAPI):
#     print('before the table creation')
#     create_table()
#     yield


# app: FastAPI = FastAPI(lifespan=beforeStarting)


# def get_session():
#     with Session as session:
#         yield session


# connection_String: str = str(settings.DATA_BASE_URL).replace(
#     "postgresql", "postgresql + psycopg2")
# engine = create_engine(connection_String, connect_args={
#                        "sslmode": "require", }, pool_recycle=300)


# def create_table():
#     model.User.metadata.create_all(engine)

app: FastAPI = FastAPI( )
@app.get('/')
def home_city():
    return {'message': model.name }


@app.get('/cities', response_model=dict[str, list[str]])
def get_cities():
    return {'Cities': ['lahore', 'sialkot', 'daska']}


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == '__main__':
    main()
