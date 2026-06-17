from sqlalchemy import Boolean, Column, Integer, String

from app.core.database import Base


class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String(150), nullable=False)

    plataforma = Column(String(50), nullable=False)

    genero = Column(String(50), nullable=False)

    ano_lancamento = Column(Integer)

    disponivel = Column(Boolean, default=True)