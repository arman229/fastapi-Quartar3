     
   
from fastapi import FastAPI,Depends,  HTTPException  
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
ALGORITHM = "HS256"
SECRET_KEY = "A Secure Secret Key"

app = FastAPI(title='Login Portal')
fake_users_db: dict[str, dict[str, str]] = {
    "ameenalam": {
        "username": "ameenalam",
        "full_name": "Ameen Alam",
        "email": "ameenalam@example.com",
        "password": "ameenalamsecret",
    },
    "mjunaid": {
        "username": "mjunaid",
        "full_name": "Muhammad Junaid",
        "email": "mjunaid@example.com",
        "password": "mjunaidsecret",
    },
}
@app.get('/')
def hello_world():
    return {'message':"helloworld"}

def create_access_token(username: str, validation_time: timedelta) -> str:
    expiry_minutes = datetime.utcnow() + validation_time
    json_data = {"sub": username, "exp": expiry_minutes}
    encoded_jwt = jwt.encode(json_data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
  
 
 
@app.get("/get_token")
def call_access_token(username: str) -> dict[str, str]:
    validation_time = timedelta(minutes=1)
    token_value = create_access_token(username=username, validation_time=validation_time)
    return {"Token Value": token_value}


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print(e)
        return {"error": e}
@app.get("/decode_token")
def decode_token_call(token:str):
    return decode_token(token)
# @app.post("/login")
# def login_portal(data_from_user:Annotated[OAuth2PasswordRequestForm,Depends(OAuth2PasswordRequestForm)]):
#     username = data_from_user.username
#     password = data_from_user.password
#     if username == "admin" and password == "123":
#         token = create_access_token(username=username, validation_time=timedelta(minutes=1))
#         return {"token": token}
#     else:
#         return {"error": "Invalid Credentials"}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]):
    """
    Understanding the login system
    -> Takes form_data that have username and password
    """
    user_in_fake_db = fake_users_db.get(form_data.username)
    if not user_in_fake_db:
        raise HTTPException(status_code=400, detail="Incorrect username")

    if not form_data.password == user_in_fake_db["password"]:
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token_expires = timedelta(minutes=1)

    access_token = create_access_token(
        username=user_in_fake_db["username"], validation_time=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer", "expires_in": access_token_expires.total_seconds() }    
    
@app.get("/users/all")
def get_all_users(token:Annotated[str,Depends(oauth2_scheme)]):
    # Note: We never return passwords in a real application
    return fake_users_db

@app.get("/users/me")
def read_users_me(token: Annotated[str, Depends(oauth2_scheme)]):
    user_token_data = decode_token_call(token)
    
    user_in_db = fake_users_db.get(user_token_data["sub"])
    
    return user_in_db    