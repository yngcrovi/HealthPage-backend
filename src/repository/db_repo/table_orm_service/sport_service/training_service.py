from src.repository.db_repo.table_orm_service.sport_service.addit_info_training_service import AdditionalInfoTrainingService
from src.repository.tables.training import Training
from src.repository.dto import UserGetDTO, UserPostDTO, UserParamDTO

class TrainingService(AdditionalInfoTrainingService): 

    def __init__(self) -> None:
        self.table = Training

    async def insert_training(self, insert_data: dict | list) -> Training:
        value = await self.insert_data(insert_data)
        return value  
    
training_service = TrainingService()