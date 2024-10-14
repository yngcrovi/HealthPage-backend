from src.repository.model.model_sport import ExerciseModel
from src.repository.postgres.postgres import PostgreSQLRepository
from src.repository.service.dto_form.dto_form import IdGetDTO

class ExerciseService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def select_id_exercise(self, filter_data: dict) -> list[IdGetDTO] | IdGetDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(IdGetDTO, res)
        return result_dto.id

exercise_service = ExerciseService(ExerciseModel)