from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
from src.repository.tables.refresh_token import RefreshToken
from repository.dto import TokenGetDTO
import asyncio


class RefreshTokenService(PostgreSQLRepository): 

    def __init__(self, table):
        self.table = table

    async def select_token(self, filter_data: dict) -> TokenGetDTO:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(TokenGetDTO, res)
        return result_dto
    
    async def insert_refresh_token(self, insert_data: dict | list) -> RefreshToken:
        value = await self.insert_data(insert_data)
        return value

refresh_token_service = RefreshTokenService(RefreshToken)