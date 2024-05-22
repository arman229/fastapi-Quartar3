from fastapi import FastAPI, Form, Depends, HTTPException, Header
from sqlmodel import Session, select
from backend_authportal.setting import DATA_BASE_URL
from backend_authportal.model import Users, Todo
from typing import Annotated, Optional
from datetime import timedelta
from backend_authportal.token_utils import create_access_token, verify_token_expiry
from backend_authportal.database import get_session

# poetry run uvicorn backend_authportal.newmain:app
app = FastAPI(title='Login Portal')


@app.post('/signup')
def signup(session: Annotated[Session, Depends(get_session)],
           email: Annotated[str, Form()],
           password: Annotated[str, Form()],
           phone: Annotated[str, Form()],
           full_name: Annotated[str, Form()]):
    user = Users(email=email, password=password,
                 phone=phone, full_name=full_name)

    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": f"User on this email {email} created successfully"}


@app.post("/signin")
def signin(session: Annotated[Session, Depends(get_session)], email: Annotated[str, Form()],
           password: Annotated[str, Form()]):
    statement = select(Users).where((Users.email == email)
                                    & (Users.password == password))
    user = session.exec(statement).first()
    if not user:
        raise HTTPException(
            status_code=401, detail="Invalid email or password")
    access_token = create_access_token(
        name=user.full_name,
        subject=user.email,
        expires_delta=timedelta(minutes=2)
    )
    user.token = access_token
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"token": access_token}


@app.post("/signout")
def signout(session: Annotated[Session, Depends(get_session)], authorization: Optional[str] = Header(None)):
    statement = select(Users).where(Users.token == authorization)
    user = session.exec(statement).first()
    if user:
        user.token = None
        session.add(user)
        session.commit()
        session.refresh(user)
    return {"message": "Successfully signed out"}


@app.get("/todos")
def home(session: Annotated[Session, Depends(get_session)], authorization: Optional[str] = Header(None)):
    if authorization is None:
        raise HTTPException(
            status_code=401, detail="Authorization header is missing")
    is_valid, message = verify_token_expiry(authorization)
    # if not is_valid:
    #     raise HTTPException(status_code=401, detail=message)
    statement = select(Todo)
    todos = session.exec(statement).all()
    return {"todos ": todos}
