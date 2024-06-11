from fastapi import FastAPI, Form, Depends, HTTPException, Header
from sqlmodel import Session, select
from backend_authportal.setting import DATA_BASE_URL
from backend_authportal.model import NewUsers
from typing import Annotated, Optional
from datetime import timedelta
# from backend_authportal.token_utils import create_access_token, verify_token_expiry
from backend_authportal.database import get_session
from backend_authportal.creating_tables import create_tables
from backend_authportal.creating_tables import lifespan

app = FastAPI(lifespan=lifespan,title='Login Portal')


# @app.post('/signup')
# def signup(session: Annotated[Session, Depends(get_session)],
#            email: Annotated[str, Form()],
#            password: Annotated[str, Form()],
#            phone: Annotated[str, Form()],
#            user_name: Annotated[str, Form()]):
#     user = NewUsers(email=email, password=password,
#                  phone=phone, user_name=user_name)

#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return {"message": f"User on this email {email} created successfully"}

@app.post('/signup')
def signup(session: Annotated[Session, Depends(get_session)],
           email: Annotated[str, Form()],
           password: Annotated[str, Form()],
           phone: Annotated[str, Form()],
           user_name: Annotated[str, Form()]):
     
    existing_user = session.exec(select(NewUsers).where(NewUsers.email == email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail=f"Email {email} is already in use.")
 
    
    # Check if username already exists
    existing_user = session.exec(select(NewUsers).where(NewUsers.user_name == user_name)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail=f"Username {user_name} is already in use.")

    # If all checks pass, create the new user
    user = NewUsers(email=email, password=password, phone=phone, user_name=user_name)

    try:
        session.add(user)
        session.commit()
        session.refresh(user)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="An error occurred while creating the user.")

    return {"message": f"User with email {email} created successfully"}

# @app.post("/signin")
# def signin(session: Annotated[Session, Depends(get_session)], email: Annotated[str, Form()],
#            password: Annotated[str, Form()]):
#     statement = select(Users).where((Users.email == email)
#                                     & (Users.password == password))
#     user = session.exec(statement).first()
#     if not user:
#         raise HTTPException(
#             status_code=401, detail="Invalid email or password")
#     access_token = create_access_token(
#         name=user.full_name,
#         subject=user.email,
#         expires_delta=timedelta(minutes=2)
#     )
#     user.token = access_token
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return {"token": access_token}


# @app.post("/signout")
# def signout(session: Annotated[Session, Depends(get_session)], authorization: Optional[str] = Header(None)):
#     statement = select(Users).where(Users.token == authorization)
#     user = session.exec(statement).first()
#     if user:
#         user.token = None
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#     return {"message": "Successfully signed out"}





@app.get("/mainpage")
def main():
    return {"message": "Welcome to main page"}























# @app.get("/todos")
# def home(session: Annotated[Session, Depends(get_session)], authorization: Optional[str] = Header(None)):
#     if authorization is None:
#         raise HTTPException(
#             status_code=401, detail="Authorization header is missing")
#     is_valid, message = verify_token_expiry(authorization)
#     # if not is_valid:
#     #     raise HTTPException(status_code=401, detail=message)
#     statement = select(Todo)
#     todos = session.exec(statement).all()
#     return {"todos ": todos}
