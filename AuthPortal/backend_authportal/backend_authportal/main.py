from fastapi import FastAPI, Depends, Form, HTTPException, Security ,Response 
from sqlmodel import Session, select
from typing import Annotated
from backend_authportal.creating_tables import newlifespan
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from backend_authportal.model import NewUsers, UserClass, UserResponse
from backend_authportal.database import get_session
from fastapi.middleware.cors import CORSMiddleware

from backend_authportal.token_utils import (
    get_password_hash,
    create_access_token,
    verify_password,
    verify_token,
    get_current_user,
)


app = FastAPI(
    lifespan=newlifespan,
    title="Hello World API with DB",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"message": "Hello world!"}


@app.post("/api/signup")
def signup(
    username: Annotated[str, Form()],
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
    phone: Annotated[str, Form()],
    session: Annotated[Session, Depends(get_session)],
):
    db_user = session.exec(
        select(NewUsers).where(NewUsers.username == username)
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(password)
    add_new_user = NewUsers(
        username=username, email=email, hashed_password=hashed_password, phone=phone
    )
    try:
        session.add(add_new_user)
        session.commit()
        session.refresh(add_new_user)
    except:
        raise HTTPException(
            status_code=400, detail="An error occurred while creating the user."
        )

    return {"message": f"User with email {email} created successfully"}
@app.post("api/validation_token")
def validate_token(token,str,session: Annotated[Session, Depends(get_session)],):
    user = get_current_user(token,session)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": f"Token is valid and user: {user}"}

@app.post("/api/signin")
def signin(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)],
    session: Annotated[Session, Depends(get_session)],
    response: Response
): 
   
    db_user = session.exec(
        select(NewUsers).where(NewUsers.username == form_data.username)
    ).first()
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.username})
    db_user.token = access_token
    session.add(db_user)
    session.commit()
    # response.set_cookie(key="auth_token", value=access_token, httponly=True, secure=False, samesite='lax')

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": "Login Successfully",
    }


@app.post("/signout")
def signout(
    token: Annotated[str, Depends(verify_token)],
    session: Annotated[Session, Depends(get_session)],
):
    print(f"signout token is {token}")
    user = get_current_user(token, session)
    if user:
        user.token = None
        session.add(user)
        session.commit()
    return {"message": f"Successfully signed out and token is {token} user:{user}"}


@app.get("/products/")
def read_products(token: Annotated[str, Depends(verify_token)]):
    return {"products": ["Product 1", "Product 2", "Product 3"]}


@app.get("/newproducts/")
def read_newproducts(token: Annotated[str, Depends(verify_token)]):
    return {"products": ["Product 1", "Product 2", "Product 3"]}
