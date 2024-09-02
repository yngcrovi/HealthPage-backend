from src.repository.tables.part_of_body import PartOfBody
from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
from src.repository.dto import IdGetDTO


class PartOfBodyService(PostgreSQLRepository): 

    def __init__(self) -> None:
        self.table = PartOfBody

    async def select_id_pob(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id

part_of_body_service = PartOfBodyService()