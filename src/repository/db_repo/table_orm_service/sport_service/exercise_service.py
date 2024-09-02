from src.repository.tables.exercise import Exercise
from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
from src.repository.dto import IdGetDTO

class ExerciseService(PostgreSQLRepository): 

    def __init__(self) -> None:
        self.table = Exercise

    async def select_id_exercise(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id

exercise_service = ExerciseService()