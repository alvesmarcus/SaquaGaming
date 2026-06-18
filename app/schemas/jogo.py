from datetime import datetime

from pydantic import (
    BaseModel,
    field_validator
)


class JogoCreate(BaseModel):
    titulo: str
    plataforma: str
    genero: str
    ano_lancamento: int

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, value):
        if len(value.strip()) < 3:
            raise ValueError(
                "O título deve ter pelo menos 3 caracteres"
            )
        return value

    @field_validator("ano_lancamento")
    @classmethod
    def validar_ano(cls, value):
        if value < 1950:
            raise ValueError(
                "Ano de lançamento inválido"
            )
        return value


class JogoResponse(BaseModel):
    id: int
    titulo: str
    plataforma: str
    genero: str
    ano_lancamento: int
    disponivel: bool

    class Config:
        from_attributes = True