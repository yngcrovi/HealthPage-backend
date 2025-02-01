from fastapi import APIRouter, Depends, Cookie
from fastapi.responses import JSONResponse
from typing import Annotated
from src.repository.service.sport_service.sport_data_service import SportDataService
from src.repository.model.model_sport import *
from src.auth.token_decode import decode_user_token_for_data
from pydantic import BaseModel

route = APIRouter(
    tags=['Get sport data'],
    prefix='/get_sport_data'
)

@route.get("/load_type")
async def get_sport_data(
    user_data: Annotated[dict, Depends(decode_user_token_for_data)]
) -> JSONResponse:

    response = JSONResponse(
        content={
        },
        status_code=200
    )
    return response