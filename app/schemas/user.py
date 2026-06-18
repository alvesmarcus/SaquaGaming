from datetime import datetime

from pydantic import (
    BaseModel,
    EmailStr,
    field_validator
)


class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, value):
        if len(value.strip()) < 3:
            raise ValueError(
                "O nome deve ter pelo menos 3 caracteres"
            )
        return value

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, value):
        if len(value) < 6:
            raise ValueError(
                "A senha deve ter pelo menos 6 caracteres"
            )
        return value


class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    ativo: bool
    created_at: datetime

    class Config:
        from_attributes = True