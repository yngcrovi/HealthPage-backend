from src.repository.model.model_sport import *
from src.repository.postgres.postgres import PostgreSQLRepository
from src.repository.service.dto_form.dto_form import IdGetDTO


class SportDataService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table


    async def select(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id
    

#Передать лт, поб и пом и сджоинить их в инит скорее всего
# part_of_body_service = SportDataService(LoadTypeModel, PartOfBodyModel, PartOfMuscleModel)

