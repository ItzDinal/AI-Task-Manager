from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    username: str

    class config: 
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TOkenData(BaseModel):
    sub: str | None = None
