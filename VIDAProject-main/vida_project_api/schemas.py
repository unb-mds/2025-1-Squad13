from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    voice: Optional[str]

class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: EmailStr