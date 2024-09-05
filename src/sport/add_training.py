from pydantic import BaseModel
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
import datetime
from typing import Annotated
from src.auth_user.token import decode_user_token_for_data
from src.repository.db_repo.table_orm_service.sport_service.training_service import training_service
from src.repository.db_repo.table_orm_service.sport_service.addit_info_training_service import addit_info_training_service
from src.repository.db_repo.table_orm_service.sport_service.load_type_service import load_type_service
from src.repository.db_repo.table_orm_service.sport_service.exercise_service import exercise_service

route = APIRouter(
    prefix='/add_training',
    tags=['Add training'],
)

class TrainingData(BaseModel):
    load_type: str
    exercise: list[str]
    type_weight: list[str]
    weight: list[float]
    number_of_repetitions: list[list[int]]

class AdditInfoTrainingData(BaseModel):
    date: datetime.date
    calories: int = None
    time_training_start: datetime.time = None
    time_training_finish: datetime.time = None
    comment: str

@route.post("")
# @cache(expire=10)
async def add_training(
    training_data: TrainingData, 
    addit_info_training_data: AdditInfoTrainingData,
    user_data: Annotated[dict, Depends(decode_user_token_for_data)]
) -> JSONResponse:
    training_data = training_data.model_dump()
    addit_info_training_data = addit_info_training_data.model_dump()
    id_load_type = await load_type_service.select_id_lt({'load_type': training_data['load_type']})
    addit_info_training_data['id_load_type'] = id_load_type
    addit_info_training_data['id_username'] = user_data['id']
    id_addit_info_trainint = await addit_info_training_service.insert_addit_info_training(addit_info_training_data)
    training_data['id_additional_info_training'] = id_addit_info_trainint.id
    del training_data['load_type'] 
    for i in range(len(training_data['exercise'])):
        exercise = {
            'exercise': training_data['exercise'][i]
        }
        training_data['exercise'][i] = await exercise_service.select_id_exercise(exercise)
    #Передать на фронте без лишнего массива training_data['number_of_repetision']
    for i in range(len(training_data['number_of_repetitions'])-1):
        training = {}
        training['id_username'] = user_data['id']
        training['id_additional_info_training'] = training_data['id_additional_info_training']
        training['id_exercise'] = training_data['exercise'][i]
        training['weight'] = training_data['weight'][i]
        training['type_weight'] = training_data['type_weight'][i]
        for j in training_data['number_of_repetitions'][i]:
            training['number_of_repetitions'] = j
            training['approach_numbers'] = i+1
            await training_service.insert_training(training)
    response = JSONResponse(
        content={
            'detail': 'ok'
        },
        status_code=200
    )
    return response