from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.repository.tables.declarative_base import Base

class UserSalt(Base): 
    __tablename__ = 'user_salt'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(ForeignKey('user.id'))
    salt: Mapped[bytes]

    repr_cols_num = 3