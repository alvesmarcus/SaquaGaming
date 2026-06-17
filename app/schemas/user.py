from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str


class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    ativo: bool
    created_at: datetime

    class Config:
        from_attributes = True