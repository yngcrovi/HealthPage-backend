from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.repository.model.declarative_base import Base
from enum import Enum
from datetime import datetime, date

class SexType(Enum): 
    man = 'man'
    woman = 'woman'

class UserModel(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'user'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    hash_password: Mapped[bytes] = mapped_column(nullable=False)
    salt: Mapped[bytes]
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    date_of_birthday: Mapped[date] = mapped_column(nullable=False)
    sex: Mapped[SexType]
    weight: Mapped[float | None]
    height: Mapped[int | None]
    date_registration: Mapped[datetime] = mapped_column(default=datetime.now)

    repr_cols_num = 3


class RefreshTokenModel(Base): 
    __tablename__ = 'refresh_token'
    __table_args__ = {'schema': 'user'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(ForeignKey('user.user.id'))
    refresh_token: Mapped[str]
    datetime_create: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

    repr_cols_num = 3