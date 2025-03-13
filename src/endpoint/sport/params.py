from pydantic import BaseModel
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
import datetime
from typing import Annotated
from src.auth.token_decode import decode_user_token_for_data
from src.repository.service.sport_service.training_service import training_service
from src.repository.service.sport_service.addit_info_training_service import addit_info_training_service
from src.repository.service.sport_service.load_type_service import load_type_service
from src.repository.service.sport_service.exercise_service import exercise_service


route = APIRouter(
    prefix='',
    tags=['Sport params'],
)

@route.get("/get_load_type")
async def get_load_type(user_data: Annotated[dict, Depends(decode_user_token_for_data)]):
    print('Тут')