from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.repository.model.declarative_base import Base
from enum import Enum
import datetime

class ExerciseModel(Base):
    __tablename__ = 'exercise'
    __table_args__ = {'schema': 'sport'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(nullable=False)
    exercise: Mapped[str]
    id_part_of_body: Mapped[int] = mapped_column(ForeignKey('sport.part_of_body.id'), nullable=False)
    id_part_of_muscle: Mapped[int | None]
    id_load_type: Mapped[int] = mapped_column(ForeignKey('sport.load_type.id'), nullable=False)

    repr_cols_num = 3

class PartOfBodyModel(Base):
    __tablename__ = 'part_of_body'
    __table_args__ = {'schema': 'sport'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    part_of_body: Mapped[str] = mapped_column(nullable=False)

    repr_cols_num = 3

class PartOfMuscleModel(Base):
    __tablename__ = 'part_of_muscle'
    __table_args__ = {'schema': 'sport'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_part_of_body: Mapped[int] = mapped_column(nullable=False) 
    part_of_muscle: Mapped[str] = mapped_column(nullable=False)
    
    #TODO: Выяснить, для чего нужен и почему при таком сценарии ошибка
    # part_of_body = relationship('sport.part_of_body')

    repr_cols_num = 3

class LoadTypeModel(Base):
    __tablename__ = 'load_type'
    __table_args__ = {'schema': 'sport'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(nullable=False)
    load_type: Mapped[str] = mapped_column(nullable=False)

    repr_cols_num = 3

class TypeWeight(Enum):
    kg = 'kg'
    ibs = 'ibs'

class TypeDist(Enum):
    m = 'm'
    km = 'km'

class TrainingModel(Base):
    __tablename__ = 'training'
    __table_args__ = {'schema': 'sport'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(ForeignKey('user.user.id'), nullable=False)
    id_exercise: Mapped[int] = mapped_column(ForeignKey('sport.exercise.id'), nullable=False)
    weight: Mapped[float] = mapped_column(default=0)
    type_weight: Mapped[TypeWeight | None]
    approach_numbers: Mapped[int | None]
    number_of_repetitions: Mapped[int | None]
    dist: Mapped[float | None]
    type_dist: Mapped[TypeDist | None]
    time: Mapped[datetime.time| None]
    id_additional_info_training: Mapped[int] = mapped_column(ForeignKey('sport.additional_info_training.id'))

    repr_cols_num = 3

class AdditionalInfoTrainingModel(Base):
    __tablename__ = 'additional_info_training'
    __table_args__ = {'schema': 'sport'} 

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_username: Mapped[int] = mapped_column(ForeignKey('user.user.id'), nullable=False)
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    id_load_type: Mapped[int] = mapped_column(ForeignKey('sport.load_type.id'), nullable=False)
    calories: Mapped[int | None]
    time_training_start: Mapped[datetime.time | None]
    time_training_finish: Mapped[datetime.time | None]
    tonnage: Mapped[float | None]
    comment: Mapped[str | None]

    repr_cols_num = 3