from fastapi import APIRouter, Cookie, HTTPException, status
from jose import JWTError, jwt
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import time
from repository.db_repo.table_orm_service.user_service.user_service import user_service
from repository.db_repo.table_orm_service.user_service.refresh_token_service import refresh_token_service

route = APIRouter(
    tags=['Token']
)

class RefreshToken(BaseModel):
    refresh_token: str

SECRET_KEY = "0831c245e79aef31076e81414958a9cdc244622b002a478da705b18b375bf065"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECOND = 60*10
REFRESH_TOKEN_EXPIRE_SECOND = 60*60*24*31
REFRESH_TOKEN_EXPIRE_SECOND_LONG = 60*60*24*31*3

def decode_token(token: str) -> dict | bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return False    

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
    
@route.post('/refresh_access')
async def refresh_access(
    refresh_token: RefreshToken
):
    payload = decode_token(refresh_token.refresh_token)
    if payload:
        access_token = get_access_token(payload)
        response = JSONResponse(
        content = {
            'response': 'Пользователь создан!',
            'refresh_token': f'{refresh_token}'
            }, 
            status_code = 200
        )
        response.set_cookie(key='access_token', value=f'{access_token}', httponly=True)
        return response