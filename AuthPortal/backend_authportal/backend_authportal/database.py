from sqlmodel import create_engine, Session, SQLModel
from backend_authportal.model import Users
from backend_authportal.setting import DATA_BASE_URL
engine = create_engine(str(DATA_BASE_URL),  pool_recycle=300)


def get_session():
    with Session(engine) as session:
        yield session
