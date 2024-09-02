from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status, Response, Request, Header, Cookie
from fastapi.requests import Request
from pydantic import BaseModel
from auth_user.token import decode_token

route = APIRouter()

class UserPayload(BaseModel):
    id: int
    username: str

async def get_current_user(access_token: str = Cookie()):
    user = decode_token(access_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    return user

@route.get("/me")
async def read_users_me(
    current_user: Annotated[UserPayload, Depends(get_current_user)],
):
    print(current_user)
    return current_user