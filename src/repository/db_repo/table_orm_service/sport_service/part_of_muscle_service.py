from src.repository.tables.part_of_muscle import PartOfMuscle
from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
from src.repository.dto import IdGetDTO


class PartOfMuscleService(PostgreSQLRepository): 

    def __init__(self) -> None:
        self.table = PartOfMuscle

    async def select_id_pom(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id

part_of_muscle_service = PartOfMuscleService()