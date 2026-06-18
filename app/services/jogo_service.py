from sqlalchemy.orm import Session

from app.repositories.jogo_repository import (
    create_jogo,
    get_all_jogos,
    get_jogo_by_id
)


def criar_jogo(
    db: Session,
    titulo: str,
    plataforma: str,
    genero: str,
    ano_lancamento: int
):
    return create_jogo(
        db=db,
        titulo=titulo,
        plataforma=plataforma,
        genero=genero,
        ano_lancamento=ano_lancamento
    )


def listar_jogos(
    db: Session,
    limit: int = 10,
    offset: int = 0,
    plataforma: str | None = None,
    disponivel: bool | None = None
):
    return get_all_jogos(
        db=db,
        limit=limit,
        offset=offset,
        plataforma=plataforma,
        disponivel=disponivel
    )


def buscar_jogo_por_id(
    db: Session,
    jogo_id: int
):
    return get_jogo_by_id(db, jogo_id)