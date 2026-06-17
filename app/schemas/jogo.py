from pydantic import BaseModel


class JogoCreate(BaseModel):
    titulo: str
    plataforma: str
    genero: str
    ano_lancamento: int


class JogoResponse(BaseModel):
    id: int
    titulo: str
    plataforma: str
    genero: str
    ano_lancamento: int
    disponivel: bool

    class Config:
        from_attributes = True