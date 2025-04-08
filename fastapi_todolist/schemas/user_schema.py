from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool = True
    is_superuser: bool = False


class UserResponseSchema(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
