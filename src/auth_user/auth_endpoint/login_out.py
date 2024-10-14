from fastapi import APIRouter, HTTPException, status, Depends, Cookie
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Annotated
from src.auth_user.hash_password import compare_hesh_password
from src.auth_user.token.token_factory import get_access_token, get_refresh_token
from src.repository.service.user_service.user_service import user_service
from src.repository.service.user_service.refresh_token_service import refresh_token_service
from dotenv import load_dotenv
import os

load_dotenv()

COOKIE_EXPIRES_ACCESS_TOKEN = os.getenv("COOKIE_EXPIRES_ACCESS_TOKEN")


route = APIRouter(
    tags=['Login_out']
)

class UserLogin(BaseModel):
    username: str
    password: str
    exp_refresh: bool

async def user_exists(user: UserLogin) -> UserLogin:
    username = {'username': user.username}
    check_exist = await user_service.select_user(username)
    if check_exist:
        user = user.model_dump()
        user['hash_password'] = check_exist.hash_password
        user['id'] = check_exist.id
        user['salt'] = check_exist.salt
        return user
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not exists",
        )
    
@route.post("/login")
async def login(
    user_data: Annotated[dict, Depends(user_exists)],
) -> JSONResponse:
    if not compare_hesh_password(user_data['password'], user_data['salt'], user_data['hash_password']):
        return JSONResponse(content = {'response': 'Пароль не совпадает!'}, status_code = 401)
    access_token = get_access_token(user_data)
    refresh_token = get_refresh_token(user_data, user_data['exp_refresh'])
    await refresh_token_service.update_token(
            user_data['id'],
            {'refresh_token': refresh_token}
        )
    response = JSONResponse(
        content = {
            'response': 'Успешный вход!',
            'refresh_token': f'{refresh_token}'
            }, 
            status_code = 200
        )
    response.set_cookie(
        key='access_token', 
        value=access_token, 
        httponly=True, 
        samesite='None', 
        secure=True, 
        expires=int(COOKIE_EXPIRES_ACCESS_TOKEN)
    )
    return response

@route.post("/logout")
async def logout(
    access_token: str = Cookie()
) -> JSONResponse:
    response = JSONResponse(content = {'response': 'Успешный выход!'}, status_code = 200)
    response.delete_cookie(
        key='access_token', 
        httponly=True, 
        samesite='None', 
        secure=True
    )
    return response