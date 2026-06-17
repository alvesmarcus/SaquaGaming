from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.sql import func

from app.core.database import Base


class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    jogo_id = Column(
        Integer,
        ForeignKey("jogos.id"),
        nullable=False
    )

    data_emprestimo = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    data_devolucao = Column(
        DateTime(timezone=True),
        nullable=True
    )

    devolvido = Column(
        Boolean,
        default=False
    )