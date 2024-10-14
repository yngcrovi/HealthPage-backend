from src.repository.postgres.postgres import PostgreSQLRepository
from src.repository.model.model_user import RefreshTokenModel
from src.repository.service.dto_form.dto_form import TokenGetDTO


class RefreshTokenService(PostgreSQLRepository): 

    def __init__(self, table):
        self.table = table

    async def select_token(self, filter_data: dict) -> TokenGetDTO:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(TokenGetDTO, res)
        return result_dto
    
    async def insert_refresh_token(self, insert_data: dict | list) -> RefreshTokenModel:
        value = await self.insert_data(insert_data)
        return value

    async def update_token(self, upd_id: int, upd_data: dict) -> None:
        await self.update_data(upd_id, upd_data)

refresh_token_service = RefreshTokenService(RefreshTokenModel)