from fastapi import FastAPI
import uvicorn
 
from backend_authportal import model
from jose import jwt, JWTError
from datetime import datetime, timedelta
 

ALGORITHM:str = 'ARMAN'
SECRET_KEY:str = 'My name is arman'
def create_access_token(subject: str , expires_delta: timedelta) -> str:
    # utcnow:to  get current date 
    expire = datetime.utcnow() + expires_delta
    # such as name in my libraty card name:sub
    to_encode = {"expiry_time": expire, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

app: FastAPI = FastAPI( )
@app.get('/')
def home_city():
    return {'message': model.name }


@app.get("/get_token")
def get_access_token(user_name: str):
    
    access_token_expires = timedelta(minutes=1)
    
    access_token = create_access_token(subject=user_name, expires_delta=access_token_expires)
    
    return {"access_token": access_token}

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == '__main__':
    main()
