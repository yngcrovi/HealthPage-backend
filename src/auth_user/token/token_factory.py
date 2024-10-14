from jose import jwt
import time
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_SECOND = int(os.getenv("ACCESS_TOKEN_EXPIRE_SECOND"))
REFRESH_TOKEN_EXPIRE_SECOND = int(os.getenv("REFRESH_TOKEN_EXPIRE_SECOND"))
REFRESH_TOKEN_EXPIRE_SECOND_LONG = int(os.getenv("REFRESH_TOKEN_EXPIRE_SECOND_LONG"))

def create_token(data: dict, time_expires: float) -> str:
    data.update({"exp": time_expires})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_access_token(token_data: dict) -> str:
    access_token_expires = time.time() + ACCESS_TOKEN_EXPIRE_SECOND
    access_token = create_token(data={'id': token_data['id'], 'username': token_data['username']}, time_expires=access_token_expires)
    return access_token

def create_refresh_token(token_data: dict, exp) -> str:
    if exp:
        refresh_token_expires = time.time() + REFRESH_TOKEN_EXPIRE_SECOND_LONG
    else:
        refresh_token_expires = time.time() + REFRESH_TOKEN_EXPIRE_SECOND
    refresh_token = create_token(data={'id': token_data['id'], 'username': token_data['username']}, time_expires=refresh_token_expires)
    return refresh_token
    
def get_access_token(user_data: dict) -> str:
    token = create_access_token(user_data)
    return token

def get_refresh_token(user_data: dict, exp: bool) -> str:
    token = create_refresh_token(user_data, exp)
    return token