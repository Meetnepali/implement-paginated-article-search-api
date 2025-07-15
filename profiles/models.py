from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 32
AGE_MIN = 13
AGE_MAX = 120

class UserProfileBase(BaseModel):
    username: str = Field(..., min_length=USERNAME_MIN_LENGTH, max_length=USERNAME_MAX_LENGTH, regex=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    age: int = Field(..., ge=AGE_MIN, le=AGE_MAX)

    @validator('username')
    def no_forbidden_names(cls, v):
        forbidden = {"admin", "root", "me"}
        if v.lower() in forbidden:
            raise ValueError("username is forbidden")
        return v

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(BaseModel):
    email: Optional[EmailStr]
    age: Optional[int] = Field(None, ge=AGE_MIN, le=AGE_MAX)

class UserProfile(UserProfileBase):
    class Config:
        orm_mode = True