from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
from src.repository.tables.user import User
import asyncio
from src.repository.dto import UserGetDTO, UserPostDTO, UserParamDTO
from pydantic import BaseModel

class UserService(PostgreSQLRepository): 

    def __init__(self) -> None:
        self.table = User

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
    
    async def insert_user(self, insert_data: dict | list) -> User:
        value = await self.insert_data(insert_data)
        return value
    
    async def update_params(self, upd_id: int, upd_data: dict) -> User:
        await self.update_data(upd_id, upd_data)
   

    

user_service = UserService()




























# user_data = {
#         'username': 'qwe', 
#         'hash_password': b'\xdc1\xfd\x9f\xf2F\x19w\xa0\xc6K\x16]\x02\xec=r_\x18\xf1C/\xd2@\xae\x0f\xe2\xb9\xc4:\xba.',
#         'email': 'qwe',
#         'date_of_birthday': '2024-02-01',
#         'sex': 'man',
#     }

# test = {
#     'email': 'crovion@gmail.com',
#     'weight': 68.3
# }

# id = asyncio.run(user_service.insert_user(user_data))
# print(id.id)
# asyncio.run(a.update_data(1, test))
# body = {}
# asyncio.run(user_service.select_user({'id': 1}))
# for i in result[0]:
#     body[f'{i[0]}'] = i[1]
# print(body)