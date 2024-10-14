from src.repository.postgres.postgres import PostgreSQLRepository
from src.repository.model.model_sport import AdditionalInfoTrainingModel

class AdditionalInfoTrainingService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def insert_addit_info_training(self, insert_data: dict | list) -> AdditionalInfoTrainingModel:
        value = await self.insert_data(insert_data)
        return value
    
addit_info_training_service = AdditionalInfoTrainingService(AdditionalInfoTrainingModel)