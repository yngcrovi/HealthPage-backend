from src.repository.config.engine import engine
from src.repository.tables.declarative_base import Base
from src.repository.tables.refresh_token import RefreshToken
from src.repository.tables.user import User
from src.repository.tables.user_salt import UserSalt
from src.repository.tables.training import Training
from src.repository.tables.exercise import Exercise
from src.repository.tables.load_type import LoadType
from src.repository.tables.part_of_body import PartOfBody
from src.repository.tables.part_of_muscle import PartOfMuscle
from src.repository.tables.additional_info_training import AdditionalInfoTraining


Base.metadata.create_all(engine)

