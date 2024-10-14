from src.repository.model.model_sport import LoadTypeModel
from src.repository.postgres.postgres import PostgreSQLRepository
from src.repository.service.dto_form.dto_form import IdGetDTO

class LoadTypeService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def select_id_lt(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id
    
    async def insert_lt(self, insert_data: dict | list) -> LoadTypeModel:
        value = await self.insert_data(insert_data)
        return value  
    
    
load_type_service = LoadTypeService(LoadTypeModel)