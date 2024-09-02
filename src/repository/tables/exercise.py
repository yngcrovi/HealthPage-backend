from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, ForeignKey
from src.repository.tables.declarative_base import Base

class Exercise(Base):
    __tablename__ = 'exercise'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(nullable=False)
    exercise: Mapped[str]
    id_part_of_body: Mapped[int] = mapped_column(ForeignKey('part_of_body.id'), nullable=False)
    id_part_of_muscle: Mapped[int | None]
    id_load_type: Mapped[int] = mapped_column(ForeignKey('load_type.id'), nullable=False)

    repr_cols_num = 3