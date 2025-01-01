from fastapi import Cookie, HTTPException, status
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def decode_token(token: str) -> dict | bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return False    
    
def decode_user_token_for_data(
    access_token: str = Cookie()
):
    payload = decode_token(access_token)
    if payload:
        del payload['exp']
        return payload
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="need_refresh_access_token",
        )