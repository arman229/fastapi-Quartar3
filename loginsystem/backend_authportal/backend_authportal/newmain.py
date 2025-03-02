# from fastapi import FastAPI, Depends, Form, HTTPException, Security ,Response 
# from sqlmodel import Session, select
# from typing import Annotated
# from backend_authportal.creating_tables import newlifespan
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from passlib.context import CryptContext
# from backend_authportal.model import NewUsers, UserClass, UserResponse
# from backend_authportal.database import get_session
# from fastapi.middleware.cors import CORSMiddleware

# from backend_authportal.token_utils import (
#     get_password_hash,
#     create_access_token,
#     verify_password,
#     verify_token,
#     get_current_user,
# )

  
# app = FastAPI(
#     lifespan=newlifespan,
#     title="Hello World API with DB",
# )
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def hello():
#     return {"message": "Hello world!"}


# @app.post("/api/signup")
# def signup(
#     username: Annotated[str, Form()],
#     email: Annotated[str, Form()],
#     password: Annotated[str, Form()],
#     phone: Annotated[str, Form()],
#     session: Annotated[Session, Depends(get_session)],
# ):
#     db_user = session.exec(
#         select(NewUsers).where(NewUsers.username == username)
#     ).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     hashed_password = get_password_hash(password)
#     add_new_user = NewUsers(
#         username=username, email=email, hashed_password=hashed_password, phone=phone
#     )
#     try:
#         session.add(add_new_user)
#         session.commit()
#         session.refresh(add_new_user)
#     except:
#         raise HTTPException(
#             status_code=400, detail="An error occurred while creating the user."
#         )

#     return {"message": f"User with email {email} created successfully","status":200}

# @app.post("/api/validate_token")
# def validate_token(token: str, session: Session = Depends(get_session)):
#     user = get_current_user(token, session)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return {"valid": True, "user": user.username}
# @app.post("/api/signin")
# def signin(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)],
#     session: Annotated[Session, Depends(get_session)],
#     response: Response
# ): 
   
#     db_user = session.exec(
#         select(NewUsers).where(NewUsers.username == form_data.username)
#     ).first()
#     if not db_user or not verify_password(form_data.password, db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     access_token = create_access_token(data={"sub": db_user.username})
#     db_user.token = access_token
#     session.add(db_user)
#     session.commit()
#     # response.set_cookie(key="auth_token", value=access_token, httponly=True, secure=False, samesite='lax')

#     return {
#         "access_token": access_token,
#         "token_type": "bearer",
#         "message": "Login Successfully",
#     }


# @app.post("/api/signout")
# def signout(
#     token: Annotated[str, Depends(verify_token)],
#     session: Annotated[Session, Depends(get_session)],
# ):
#     print(f"signout token is {token}")
#     user = get_current_user(token, session)
#     if user:
#         user.token = None
#         session.add(user)
#         session.commit()
#     return {"message": f"Successfully signed out and token is {token} user:{user}"}


# @app.get("/products/")
# def read_products(token: Annotated[str, Depends(verify_token)]):
#     return {"products": ["Product 1", "Product 2", "Product 3"]}


# @app.get("/newproducts/")
# def read_newproducts(token: Annotated[str, Depends(verify_token)]):
#     return {"products": ["Product 1", "Product 2", "Product 3"]}
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Dict, List, Optional
from datetime import datetime

# Constants for token creation
SECRET_KEY = "83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# In-memory database mockup as a list with predefined admin and user
db: List[Dict] = [
    {
        "username": "admin",
        "email": "admin@example.com",
        "hashed_password": "$2b$12$ns.OChTRL0r5Jeenv3ptc.DCKUsw5QTIOAKF2RLaXBVQCavUgRzeu",  # password: "adminpassword"
        "role": "admin",
        "token": None,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "username": "tim",
        "email": "tim@gmail.com",
        "hashed_password": "$2b$12$ns.OChTRL0r5Jeenv3ptc.DCKUsw5QTIOAKF2RLaXBVQCavUgRzeu",  # password: "password"
        "role": "user",
        "token": None,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
]

# Models
class RegisterUser(BaseModel):
    username: str
    email: str
    password: str
    
class User(BaseModel):
    username: str
    email: Optional[str] = None
    role: Optional[str] = None

class UserInDB(User):
    hashed_password: str
    token: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    
class UpdateUser(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None    


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Helper Functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db: List[Dict], username: str):
    for user in db:
        if user["username"] == username:
            return UserInDB(**user)
    return None

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Token validation for current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    user = get_user(db, username=token_data.username)
    if user is None or user.token != token:  # Check if token is still valid
        raise credential_exception
    return user

# Ensure user is active
async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    return current_user

# Check if the current user is an admin
async def get_current_admin_user(current_user: UserInDB = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not have permission to access this resource.")
    return current_user


# Register endpoint
@app.post("/register/")
async def register_user(user: RegisterUser):
    if get_user(db, user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    
    # Create new user with all the required fields
    new_user = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "role": "user",  # Default role is 'user'
        "token": None,  # Initial token state is None
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    db.append(new_user)
    
    return {"message": "User registered successfully"}

# Login for token
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    
    # Update the user with the generated token and update the updated_at field
    for u in db:
        if u["username"] == user.username:
            u["token"] = access_token
            u["updated_at"] = datetime.utcnow()
    
    return {"access_token": access_token, "token_type": "bearer"}

# Logout endpoint
@app.post("/logout")
async def logout_user(current_user: UserInDB = Depends(get_current_active_user)):
    for u in db:
        if u["username"] == current_user.username:
            u["token"] = None  # Clear the token on logout
    return {"message": f"{current_user.username} has been logged out."}

# Admin-only route
@app.get("/admin/")
async def read_admin_data(current_admin_user: User = Depends(get_current_admin_user)):
    return {"message": "Welcome Admin! This is your exclusive data."}

# Get user details
@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
@app.put("/users/me/")
async def update_user_me(user_update: UpdateUser, current_user = Depends(get_current_active_user)):
    if user_update.email:
        current_user["email"] = user_update.email
    if user_update.password:
        current_user["hashed_password"] = get_password_hash(user_update.password)
    current_user["updated_at"] = datetime.utcnow()
    return {"message": "User updated successfully"}
@app.delete("/users/me/")
async def delete_user_me(current_user = Depends(get_current_active_user)):
    db.remove(current_user)
    return {"message": "User deleted successfully"}
# Get user's items
@app.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": 1, "owner": current_user}]

# Verify password hash (For Debugging)
@app.get("/hash_password")
def verify_password_debug():
    return pwd_context.verify("adminpassword", "$2b$12$ns.OChTRL0r5Jeenv3ptc.DCKUsw5QTIOAKF2RLaXBVQCavUgRzeu")

# Admin-only route to list all users
@app.get("/admin/users", response_model=List[User])
async def list_all_users(current_admin_user: User = Depends(get_current_admin_user)):
    users = []
    for user_data in db:
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            role=user_data['role']
        )
        users.append(user)
    return users

# Admin - List all users (CRUD - READ)
# @app.get("/admin/users", response_model=List[User])
# async def list_all_users(current_admin_user = Depends(get_current_admin_user)):
#     return [User(username=user["username"], email=user["email"], role=user["role"]) for user in db]

# Admin - Get specific user details (CRUD - READ)
@app.get("/admin/users/{username}", response_model=User)
async def admin_get_user(username: str, current_admin_user = Depends(get_current_admin_user)):
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return User(username=user["username"], email=user["email"], role=user["role"])

# Admin - Update user details (CRUD - UPDATE)
@app.put("/admin/users/{username}")
async def admin_update_user(username: str, user_update: UpdateUser, current_admin_user = Depends(get_current_admin_user)):
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if user_update.email:
        user["email"] = user_update.email
    if user_update.password:
        user["hashed_password"] = get_password_hash(user_update.password)
    user["updated_at"] = datetime.utcnow()
    return {"message": "User updated successfully by admin"}

# Admin - Delete a user (CRUD - DELETE)
@app.delete("/admin/users/{username}")
async def admin_delete_user(username: str, current_admin_user = Depends(get_current_admin_user)):
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.remove(user)
    return {"message": f"User {username} deleted successfully by admin"}