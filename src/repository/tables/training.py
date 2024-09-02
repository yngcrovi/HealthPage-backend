from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, ForeignKey
from src.repository.tables.declarative_base import Base
from enum import Enum
import datetime

class TypeWeight(Enum):
    kg = 'kg'
    ibs = 'ibs'

class TypeDist(Enum):
    m = 'm'
    km = 'km'

class Training(Base):
    __tablename__ = 'training'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    id_exercise: Mapped[int] = mapped_column(ForeignKey('exercise.id'), nullable=False)
    #Поставить значение по умолчанию 0
    weight: Mapped[float]
    type_weight: Mapped[TypeWeight | None]
    approach_numbers: Mapped[int | None]
    number_of_repetitions: Mapped[int | None]
    dist: Mapped[float | None]
    type_dist: Mapped[TypeDist | None]
    time: Mapped[datetime.time| None]
    id_additional_info_training: Mapped[int] =mapped_column(ForeignKey('additional_info_training.id'))


    repr_cols_num = 3

