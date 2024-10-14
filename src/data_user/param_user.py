from fastapi import APIRouter, Depends, Cookie
from fastapi.responses import JSONResponse
from typing import Annotated
from src.repository.service.user_service.user_service import user_service
from src.auth_user.token.token_decode import decode_user_token_for_data
from pydantic import BaseModel

route = APIRouter(
    tags=['Params_user']
)

class NewParams(BaseModel):
    height: int
    weight: float

@route.get("/get_params")
async def get_params(
    user_data: Annotated[dict, Depends(decode_user_token_for_data)]
) -> JSONResponse:
    user_param = await user_service.select_param(user_data)
    weight = user_param.weight
    height = user_param.height
    response = JSONResponse(
        content={
            'weight': weight,
            'height': height,
        },
        status_code=200
    )
    return response

@route.post("/update_params")
async def update_params(
    user_data: Annotated[dict, Depends(decode_user_token_for_data)],
    new_params: NewParams
) -> JSONResponse:
    new_params = new_params.model_dump()
    print(new_params)
    await user_service.update_params(user_data['id'], new_params)
    response = JSONResponse(
        content={
            'detail': 'ok'
        },
        status_code=200
    )
    return response