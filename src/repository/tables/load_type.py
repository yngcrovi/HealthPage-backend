from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, ForeignKey
from src.repository.tables.declarative_base import Base

class LoadType(Base):
    __tablename__ = 'load_type'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(nullable=False)
    load_type: Mapped[str] = mapped_column(nullable=False)

    repr_cols_num = 3