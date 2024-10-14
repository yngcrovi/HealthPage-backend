from redis import asyncio as aioredis

class Redis:
    redis: aioredis.Redis

    def __init__(self):
        self.redis = aioredis.from_url("redis://localhost")
    
    async def close_connection(self):
        await self.redis.close()

    async def get_value(self, key: str) -> bytes | str | int | dict | list:
        value = await self.redis.get(key)
        return value
    
    async def set_value(self, key: str, value, exp: int = None):
        await self.redis.set(key, value, exp)

redis = Redis()

