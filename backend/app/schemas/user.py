from pydantic import BaseModel, ConfigDict, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID
    email: str
    username: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

    model_config = ConfigDict(from_attributes=True)