from fastapi import APIRouter, Cookie, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.auth.token_decode import decode_token
from src.auth.token_factory import get_access_token
from src.redis.redis import redis
from src.repository.service.user_service.refresh_token_service import refresh_token_service
from dotenv import load_dotenv
import os

load_dotenv()

COOKIE_EXPIRES_ACCESS_TOKEN = os.getenv("COOKIE_EXPIRES_ACCESS_TOKEN")
REDIS_EXPIRES_REFRESH_TOKEN = os.getenv("REDIS_EXPIRES_REFRESH_TOKEN")

route = APIRouter(
    tags=['Token']
)

class RefreshToken(BaseModel):
    refresh_token: str

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
    refresh_token = refresh_token.model_dump()
    payload = decode_token(refresh_token['refresh_token'])
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="not auth",
        )
    refresh_from_db = await redis.get_value('refresh_token')
    if refresh_from_db:
        refresh_from_db = refresh_from_db.decode('utf-8')
        print('В кэше', refresh_from_db)
    else:
        refresh_from_db = await refresh_token_service.select_token({'id_username': payload['id']})
        refresh_from_db = refresh_from_db.model_dump()
        refresh_from_db = refresh_from_db['refresh_token']
    if not refresh_token['refresh_token'] == refresh_from_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="not compaire refresh token",
        )
    await redis.set_value('refresh_token', refresh_from_db, int(REDIS_EXPIRES_REFRESH_TOKEN))
    access_token = get_access_token(payload)
    response = JSONResponse(
    content = {
        'response': 'Пользователь создан!',
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