from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from src.sport.add_training import route as route_add_training
from src.redis.redis import redis
from src.auth_user.auth_endpoint.registratoin import route as registration
from src.auth_user.auth_endpoint.login_out import route as login_out
from src.data_user.param_user import route as param_user
from src.auth_user.token.token_endpoint import route as token

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:8000'
]

# @app.on_event("startup")
# async def startup_event():
#     Redis()
    # FastAPICache.init(RedisBackend(redis))

@app.on_event("shutdown")
async def shutdown_event():
    await redis.close_connection()

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

app.include_router(route_add_training)
app.include_router(registration)
app.include_router(login_out)
app.include_router(param_user)
app.include_router(token)
