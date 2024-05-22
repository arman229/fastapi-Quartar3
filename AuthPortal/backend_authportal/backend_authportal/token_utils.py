

from datetime import datetime, timedelta
from jose import jwt, JWTError
from backend_authportal.setting import ALGORITHM, SECRET_KEY


def create_access_token(name: str, subject: str, expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": int(expire.timestamp()),
                 "sub": subject,
                 "name": name}
    encoded_jwt = jwt.encode(to_encode, key=str(
        SECRET_KEY), algorithm=str(ALGORITHM))
    return encoded_jwt


def verify_token_expiry(token: str):
    try:
        payload = jwt.decode(token, str(SECRET_KEY), [str(ALGORITHM)])
        expiration = payload.get("exp")
        print(f"expiration: {expiration}")
        if expiration is None:
            return False, "Token does not contain expiration claim"
        if datetime.utcnow() > datetime.fromtimestamp(expiration):
            return False, "Token has expired"
        return True, "Token is valid"
    except JWTError as e:
        return False, f"Error decoding token: {e}"
