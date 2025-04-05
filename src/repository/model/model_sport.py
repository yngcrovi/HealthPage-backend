from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.repository.model.declarative_base import Base
from enum import Enum
import datetime

class BaseSportModel(Base):
    __table_args__ = {'schema': 'sport'} 
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)

class ExerciseModel(BaseSportModel):
    __tablename__ = 'exercise'

    username_id: Mapped[int] = mapped_column(ForeignKey('user.user.id'), nullable=False)
    exercise: Mapped[str] = mapped_column(unique=True)
    load_type_id: Mapped[int] = mapped_column(ForeignKey('sport.load_type.id'), nullable=False)
    part_of_body_id: Mapped[int] = mapped_column(ForeignKey('sport.part_of_body.id'), nullable=False)
    part_of_muscle_id: Mapped[int | None] = mapped_column(ForeignKey('sport.part_of_muscle.id'), nullable=False)

    user = relationship('UserModel', back_populates='exercise')
    load_type = relationship('LoadTypeModel', back_populates='exercise')
    part_of_body = relationship('PartOfBodyModel', back_populates='exercise')
    part_of_muscle = relationship('PartOfMuscleModel', back_populates='exercise')
    training = relationship('TrainingModel', back_populates='exercise')


    repr_cols_num = 3

class PartOfBodyModel(BaseSportModel):
    __tablename__ = 'part_of_body'

    part_of_body: Mapped[str] = mapped_column(nullable=False)
    
    exercise = relationship('ExerciseModel', back_populates='part_of_body')
    part_of_muscle = relationship('PartOfMuscleModel', back_populates='part_of_body')

    repr_cols_num = 3

class PartOfMuscleModel(BaseSportModel):
    __tablename__ = 'part_of_muscle'

    part_of_body_id: Mapped[int] = mapped_column(ForeignKey('sport.part_of_body.id'), nullable=False) 
    part_of_muscle: Mapped[str] = mapped_column(nullable=False)
    
    #TODO: Выяснить, для чего нужен и почему при таком сценарии ошибка
    exercise = relationship('ExerciseModel', back_populates='part_of_muscle')
    part_of_body = relationship('PartOfBodyModel', back_populates='part_of_muscle')

    repr_cols_num = 3

class LoadTypeModel(BaseSportModel):
    __tablename__ = 'load_type' 

    username_id: Mapped[int] = mapped_column(ForeignKey('user.user.id'), nullable=False)
    load_type: Mapped[str] = mapped_column(nullable=False)

    user = relationship('UserModel', back_populates='load_type')
    exercise = relationship('ExerciseModel', back_populates='load_type')
    additional_info_training = relationship('AdditionalInfoTrainingModel', back_populates='load_type')

    repr_cols_num = 3

class TypeWeight(Enum):
    kg = 'kg'
    ibs = 'ibs'

class TypeDist(Enum):
    m = 'm'
    km = 'km'

class TrainingModel(BaseSportModel):
    __tablename__ = 'training'

    username_id: Mapped[int] = mapped_column(ForeignKey('user.user.id'), nullable=False)
    exercise_id: Mapped[int] = mapped_column(ForeignKey('sport.exercise.id'), nullable=False)
    weight: Mapped[float] = mapped_column(default=0)
    type_weight: Mapped[TypeWeight | None]
    approach_numbers: Mapped[int | None]
    number_of_repetitions: Mapped[int | None]
    dist: Mapped[float | None]
    type_dist: Mapped[TypeDist | None]
    time: Mapped[datetime.time| None]
    additional_info_training_id: Mapped[int] = mapped_column(ForeignKey('sport.additional_info_training.id'))

    user = relationship('UserModel', back_populates='training')
    exercise = relationship('ExerciseModel', back_populates='training')
    additional_info_training = relationship('AdditionalInfoTrainingModel', back_populates='training')

    repr_cols_num = 3

class AdditionalInfoTrainingModel(BaseSportModel):
    __tablename__ = 'additional_info_training'

    username_id: Mapped[int] = mapped_column(ForeignKey('user.user.id'), nullable=False)
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    load_type_id: Mapped[int] = mapped_column(ForeignKey('sport.load_type.id'), nullable=False)
    calories: Mapped[int | None]
    time_training_start: Mapped[datetime.time | None]
    time_training_finish: Mapped[datetime.time | None]
    tonnage: Mapped[float | None]
    comment: Mapped[str | None]

    user = relationship('UserModel', back_populates='additional_info_training')
    load_type = relationship('LoadTypeModel', back_populates='additional_info_training')
    training = relationship('TrainingModel', back_populates='additional_info_training')

    repr_cols_num = 3