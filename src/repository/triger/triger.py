from sqlalchemy import event
from src.repository.model.model_user import UserModel
from src.repository.postgres.postgres import Base



def after_insert_listener(mapper, connection, target: UserModel):
    print(f"{mapper=}")
    print(f"{connection=}")
    print(f"{target=}")

# Подключаем триггер к событию
event.listen(UserModel, 'after_insert', after_insert_listener)