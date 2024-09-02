from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import datetime
from repository.db_repo.table_orm_service.user_service.user_service import user_service
from repository.db_repo.table_orm_service.user_service.user_salt_service import user_salt_service
from repository.db_repo.table_orm_service.user_service.refresh_token_service import refresh_token_service
from auth_user.token import get_access_token, get_refresh_token
from auth_user.hash_password import make_hesh_password
from src.repository.tables.user import SexType

route = APIRouter(
    prefix='/registration',
    tags=['Registration']
)

class UserRegistration(BaseModel):
    username: str
    password: str
    email: str
    date_of_birthday: datetime.date
    sex: SexType
    exp_refresh: bool

async def user_exists(user: UserRegistration):
    username = {'username': user.username}
    check_exist = await user_service.select_user(username)
    if check_exist:
        #Поменять код ошибки
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User exists",
        )
    else: 
        return user.model_dump()

@route.post("")
async def registration(
    #Изменить в функции селект_дата, чтобы возвращался не массив, а json файл, а потом изменить здесь на dict
    user_data: Annotated[dict, Depends(user_exists)],
) -> JSONResponse:
    key_salt = make_hesh_password(user_data['password'])
    user_data['hash_password'] = key_salt['key']
    exp_refresh_token = user_data['exp_refresh']
    del user_data['password']
    del user_data['exp_refresh']
    id_username = await user_service.insert_user(user_data)
    salt_data = {
        'id_username': id_username.id,
        'salt': key_salt['salt']
    }
    await user_salt_service.insert_salt(salt_data)
    user_data['id'] = id_username.id
    access_token = get_access_token(user_data)
    refresh_token = get_refresh_token(user_data, exp_refresh_token)
    await refresh_token_service.insert_refresh_token({'id_username': id_username.id, 'refresh_token': f'{refresh_token}'})
    response = JSONResponse(
        content = {
            'refresh_token': f'{refresh_token}',
            }, 
            status_code = 200
        )
    response.set_cookie(key='access_token', value=f'{access_token}', httponly=True)
    return response