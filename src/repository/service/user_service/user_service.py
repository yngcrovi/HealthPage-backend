from src.repository.postgres.postgres import PostgreSQLRepository
from src.repository.model.model_user import UserModel
from src.repository.service.dto_form.dto_form import UserGetDTO, UserPostDTO, UserParamDTO


class UserService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def select_user(self, filter_data: dict) -> list[UserPostDTO] | UserPostDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(UserPostDTO, res)
        return result_dto
    
    async def select_param(self, filter_data: dict) -> list[UserParamDTO] | UserParamDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(UserParamDTO, res)
        return result_dto
    
    async def insert_user(self, insert_data: dict | list) -> UserModel:
        value = await self.insert_data(insert_data)
        return value
    
    async def update_params(self, upd_id: int, upd_data: dict) -> UserModel:
        await self.update_data(upd_id, upd_data)
   

user_service = UserService(UserModel)