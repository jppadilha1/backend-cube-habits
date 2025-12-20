from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    username: str
    email: EmailStr


class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
