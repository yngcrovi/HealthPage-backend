from src.repository.db_repo.postgre_repo.postgre import PostgreSQLRepository
from src.repository.tables.additional_info_training import AdditionalInfoTraining

class AdditionalInfoTrainingService(PostgreSQLRepository): 

    def __init__(self) -> None:
        self.table = AdditionalInfoTraining

    async def insert_addit_info_training(self, insert_data: dict | list) -> AdditionalInfoTraining:
        value = await self.insert_data(insert_data)
        return value
    
addit_info_training_service = AdditionalInfoTrainingService()