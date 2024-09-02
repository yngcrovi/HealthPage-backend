from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, ForeignKey
from src.repository.tables.declarative_base import Base

class PartOfBody(Base):
    __tablename__ = 'part_of_body'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    part_of_body: Mapped[str] = mapped_column(nullable=False)

    repr_cols_num = 3