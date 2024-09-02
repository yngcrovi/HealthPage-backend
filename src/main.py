from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.sport.add_training import route as route_add_training
from src.redis.connection_redis import route as redis
from src.auth_user.authorization import route as authorization
from auth_user.registratoin import route as registration
from auth_user.login_out import route as login_out
from src.data_user.param_user import route as param_user
from src.auth_user.token import route as token


app = FastAPI()

origins = [
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

app.include_router(route_add_training)
app.include_router(redis)
app.include_router(authorization)
app.include_router(registration)
app.include_router(login_out)
app.include_router(param_user)
app.include_router(token)
