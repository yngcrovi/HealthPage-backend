from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.repository.model.declarative_base import Base
from enum import Enum
from datetime import datetime, date

class SexType(Enum): 
    man = 'man'
    woman = 'woman'

class BaseUserModel(Base):
    __table_args__ = {'schema': 'user'} 
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)

class UserModel(BaseUserModel):
    __tablename__ = 'user'

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    hash_password: Mapped[bytes] = mapped_column(nullable=False)
    salt: Mapped[bytes]
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    date_of_birthday: Mapped[date] = mapped_column(nullable=False)
    sex: Mapped[SexType]
    weight: Mapped[float | None]
    height: Mapped[int | None]
    date_registration: Mapped[datetime] = mapped_column(default=datetime.now)

    refresh_token = relationship('RefreshTokenModel', back_populates='user')
    exercise = relationship('ExerciseModel', back_populates='user')
    load_type = relationship('LoadTypeModel', back_populates='user')
    training = relationship('TrainingModel', back_populates='user')
    additional_info_training = relationship('AdditionalInfoTrainingModel', back_populates='user')

    repr_cols_num = 3


class RefreshTokenModel(BaseUserModel): 
    __tablename__ = 'refresh_token'

    username_id: Mapped[int] = mapped_column(ForeignKey('user.user.id'))
    refresh_token: Mapped[str]
    datetime_create: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

    user = relationship('UserModel', back_populates='refresh_token')

    repr_cols_num = 3