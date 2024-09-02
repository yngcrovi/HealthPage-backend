from pydantic import BaseModel


class UserPostDTO(BaseModel):
    id: int
    username: str
    hash_password: bytes

class UserParamDTO(BaseModel):
    weight: float | None
    height: int | None

class UserGetDTO(UserPostDTO):
    first_name: str
    second_name: str
    email: str

class UserSaltGetDTO(BaseModel):
    salt: bytes

class TokenGetDTO(BaseModel):
    refresh_token: str

class IdGetDTO(BaseModel):
    id: int