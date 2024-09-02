from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, ForeignKey
from src.repository.tables.declarative_base import Base

class PartOfMuscle(Base):
    __tablename__ = 'part_of_muscle'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_part_of_body: Mapped[int] = mapped_column(nullable=False)
    part_of_muscle: Mapped[str] = mapped_column(nullable=False)

    repr_cols_num = 3