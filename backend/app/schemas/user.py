from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import time
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=72)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    username: str

    preferred_start_time: Optional[time] = None
    preferred_end_time: Optional[time] = None

    model_config = { 
        "from_attributes" : True
        }
    
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: str | None = None
