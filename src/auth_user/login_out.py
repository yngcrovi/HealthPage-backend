from fastapi import APIRouter, HTTPException, status, Depends, Cookie
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Annotated
from auth_user.hash_password import compare_hesh_password
from auth_user.token import get_access_token, get_refresh_token
from repository.db_repo.table_orm_service.user_service.user_service import user_service
from repository.db_repo.table_orm_service.user_service.user_salt_service import user_salt_service


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
        user['hesh_password'] = check_exist.hash_password
        user['id'] = check_exist.id
        return user
    else: 
        #Поменять код ошибки
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not exists",
        )
    
@route.post("/login")
async def login(
    #Изменить в функции селект_дата, чтобы возвращался не массив, а json файл, а потом изменить здесь на dict
    user_data: Annotated[dict, Depends(user_exists)],
) -> JSONResponse:
    salt = await user_salt_service.select_salt({'id_username': user_data['id']})
    if not compare_hesh_password(user_data['password'], salt.salt, user_data['hesh_password']):
        return JSONResponse(content = {'response': 'Пароль не совпадает!'}, status_code = 401)
    access_token = get_access_token(user_data)
    refresh_token = get_refresh_token(user_data, user_data['exp_refresh'])
    print(refresh_token)
    response = JSONResponse(
        content = {
            'response': 'Успешный вход!',
            'refresh_token': f'{refresh_token}'
            }, 
            status_code = 200
        )
    response.set_cookie(key='access_token', value=f'{access_token}', httponly=True, domain='127.0.0.1')
    return response

@route.post("/logout")
async def logout(
    access_token: str = Cookie()
) -> JSONResponse:
    response = JSONResponse(content = {'response': 'Успешный выход!'}, status_code = 200)
    response.delete_cookie(key='access_token', httponly=True, domain='127.0.0.1')
    return response