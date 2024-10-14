from src.repository.model.model_sport import PartOfMuscleModel
from src.repository.postgres.postgres import PostgreSQLRepository
from src.repository.service.dto_form.dto_form import IdGetDTO


class PartOfMuscleService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def select_id_pom(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id

part_of_muscle_service = PartOfMuscleService(PartOfMuscleModel)