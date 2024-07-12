from sqlmodel import create_engine, Session, SQLModel
 
from backend_authportal.setting import DATA_BASE_URL
 
connection_string = str(DATA_BASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine( connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

def get_session():
    with Session(engine) as session:
        yield session
