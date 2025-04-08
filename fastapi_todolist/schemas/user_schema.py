from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: bool = True
    is_superuser: bool = False

class UserResponseSchema(BaseModel):
    name: str
    email: EmailStr
    is_active: bool
    is_superuser: bool 
