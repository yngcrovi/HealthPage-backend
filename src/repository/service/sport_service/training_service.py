from src.repository.service.sport_service.addit_info_training_service import AdditionalInfoTrainingService
from src.repository.model.model_sport import TrainingModel
from src.repository.service.dto_form.dto_form import UserGetDTO, UserPostDTO, UserParamDTO

class TrainingService(AdditionalInfoTrainingService): 

    def __init__(self, table) -> None:
        self.table = table

    async def insert_training(self, insert_data: dict | list) -> TrainingModel:
        value = await self.insert_data(insert_data)
        return value  
    
training_service = TrainingService(TrainingModel)