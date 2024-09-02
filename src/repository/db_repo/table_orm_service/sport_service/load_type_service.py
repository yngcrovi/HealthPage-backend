from src.repository.tables.load_type import LoadType
from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
import asyncio
from src.repository.dto import IdGetDTO
from pydantic import BaseModel

class LoadTypeService(PostgreSQLRepository): 

    def __init__(self) -> None:
        self.table = LoadType

    async def select_id_lt(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id
    
    async def insert_lt(self, insert_data: dict | list) -> LoadType:
        value = await self.insert_data(insert_data)
        return value  
    
    
load_type_service = LoadTypeService()