from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import Field
from typing import Optional
from src.repository.tables.tables_orm import Test

class TestFilter(Filter):
    id__gte: Optional[int] = Field(alias="id")

    class Constants(Filter.Constants):
        model = Test

    class Config:
        allow_popular_by_field_name = True
