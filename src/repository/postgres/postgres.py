from src.repository.config.engine import async_session_factory 
from sqlalchemy import select, func, cast, Integer, and_, update
from src.repository.postgres.abc_repo import AbstractRepository
from src.repository.model.declarative_base import Base
from pydantic import BaseModel
from src.repository.service.dto_form.dto_form import GetLoadTypeDTO

class PostgreSQLRepository(AbstractRepository):
    asf = async_session_factory
    table = Base

    def __init__(self, table):
        self.table = table

    async def insert_data(self, insert_data: dict | list):
        async with self.asf() as session:
            if type(insert_data) == dict:
                value = self.table(**insert_data)
                session.add(value)
            else:
                value = self.table(insert_data)
                session.add_all(insert_data)
            await session.flush()
            await session.refresh(value)
            await session.commit()
            return value

    async def select_data(
            self, filter_data: dict = {}, join_fields: list[str] = [], left_join_fields: list[str] = [], values: list[str] = []
        ):
        async with self.asf() as session:   
            query = select(self.table)
            join = [getattr(self.table, field) for field in left_join_fields]
            left_join = [getattr(self.table, field) for field in left_join_fields]
            if join:
                query = query.join(*join)
            if left_join:
                query = query.outerjoin(*left_join)
            if filter_data:
                query = query.filter_by(**filter_data)
            result = await session.execute(query)
            print(f'{result=}')
            result = result.fetchall()
            print(f'{result=}')
            result_dto = self.get_dto_form(GetLoadTypeDTO, result)
            return result_dto

    async def update_data(self, upd_id: int, upd_data: dict) -> None:
        async with self.asf() as session:
            upd = (
                update(self.table)
                .filter(self.table.id == upd_id)
                .values(upd_data)
            )
            await session.execute(upd)
            await session.commit()

    async def select_data_filter(self):
        pass

    def get_dto_form(self, dto_form: BaseModel, res: list):
        print(dto_form, res)
        result_dto = [dto_form.model_validate(row[0], from_attributes=True) for row in res]
        # if len(result_dto) == 1:
        #     result_dto = result_dto[0]
        return result_dto



