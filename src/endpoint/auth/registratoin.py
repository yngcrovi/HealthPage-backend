from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import date
from src.repository.service.user_service.user_service import user_service
from src.repository.service.user_service.refresh_token_service import refresh_token_service
from src.auth.token_factory import get_access_token, get_refresh_token
from src.auth.hash_password import make_hesh_password
from src.repository.model.model_user import SexType
from dotenv import load_dotenv
import os

load_dotenv()

COOKIE_EXPIRES_ACCESS_TOKEN = os.getenv("COOKIE_EXPIRES_ACCESS_TOKEN")

route = APIRouter(
    prefix='/registration',
    tags=['Registration']
)

class UserRegistration(BaseModel):
    username: str
    password: str
    email: str
    date_of_birthday: date
    sex: SexType
    exp_refresh: bool

async def user_exists(user_data: UserRegistration):
    check_exist = await user_service.select_user({'username': user_data.username})
    if check_exist:
        #Поменять код ошибки
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User exists",
        )
    else: 
        return user_data.model_dump()

@route.post("")
async def registration(
    user_data: Annotated[dict, Depends(user_exists)],
) -> JSONResponse:
    key_salt = make_hesh_password(user_data['password'])
    user_data['hash_password'] = key_salt['key']
    user_data['salt'] = key_salt['salt']
    exp_refresh_token = user_data['exp_refresh']
    del user_data['password']
    del user_data['exp_refresh']
    id_username = await user_service.insert_user(user_data)
    user_data['id'] = id_username.id
    access_token = get_access_token(user_data)
    refresh_token = get_refresh_token(user_data, exp_refresh_token)
    await refresh_token_service.insert_refresh_token({'username_id': id_username.id, 'refresh_token': refresh_token})
    response = JSONResponse(
        content = {
            'refresh_token': f'{refresh_token}',
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