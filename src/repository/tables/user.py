from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from src.repository.tables.declarative_base import Base
from enum import Enum
import datetime

class SexType(Enum): 
    man = 'man'
    woman = 'woman'

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    hash_password: Mapped[bytes] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    date_of_birthday: Mapped[datetime.date] = mapped_column(nullable=False)
    sex: Mapped[SexType]
    weight: Mapped[float | None]
    height: Mapped[int | None]
    date_registration: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)


    repr_cols_num = 3

