from fastapi import FastAPI
from jose import jwt, JWTError
from datetime import datetime, timedelta

ALGORITHM = "HS256"
SECRET_KEY = "A Secure Secret Key"

app = FastAPI(title='Login Portal')

@app.get('/')
def hello_world():
    return {'message':"helloworld"}

def create_access_token(username: str, validation_time: timedelta) -> str:
    expiry_minutes = datetime.utcnow() + validation_time
    json_data = {"sub": username, "exp": expiry_minutes}
    encoded_jwt = jwt.encode(json_data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
  
 
 
@app.get("/call_access_token")
def call_access_token(username: str) -> dict[str, str]:
    validation_time = timedelta(minutes=2)
    token_value = create_access_token(username=username, validation_time=validation_time)
    return {"Token Value": token_value}