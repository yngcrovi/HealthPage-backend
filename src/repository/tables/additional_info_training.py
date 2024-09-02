from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, ForeignKey
from src.repository.tables.declarative_base import Base
from enum import Enum
import datetime

class AdditionalInfoTraining(Base):
    __tablename__ = 'additional_info_training'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    id_load_type: Mapped[int] = mapped_column(ForeignKey('load_type.id'), nullable=False)
    calories: Mapped[int | None]
    time_training_start: Mapped[datetime.time | None]
    time_training_finish: Mapped[datetime.time | None]
    tonnage: Mapped[float | None]
    comment: Mapped[str | None]

    repr_cols_num = 3