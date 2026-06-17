from pydantic import BaseModel
from datetime import datetime


class EmprestimoCreate(BaseModel):
    usuario_id: int
    jogo_id: int


class EmprestimoResponse(BaseModel):
    id: int
    usuario_id: int
    jogo_id: int
    data_emprestimo: datetime
    data_devolucao: datetime | None
    devolvido: bool

    class Config:
        from_attributes = True