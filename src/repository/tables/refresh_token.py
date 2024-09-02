from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, func
from src.repository.tables.declarative_base import Base
import datetime

class RefreshToken(Base): 
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(ForeignKey('user.id'))
    refresh_token: Mapped[str]
    datetime_create: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now, onupdate=datetime.datetime.now)

    repr_cols_num = 3