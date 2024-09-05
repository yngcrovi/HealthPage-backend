from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
from src.repository.tables.user_salt import UserSalt
from repository.dto import UserSaltGetDTO
import asyncio


class UserSaltService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def select_salt(self, filter_data: dict) -> UserSaltGetDTO:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(UserSaltGetDTO, res)
        return result_dto
    
    async def insert_salt(self, insert_data: dict | list) -> UserSalt:
        value = await self.insert_data(insert_data)
        return value

user_salt_service = UserSaltService(UserSalt)