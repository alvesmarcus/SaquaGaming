from sqlalchemy.orm import Session
from app.models.jogos import Jogo


def create_jogo(
    db: Session,
    titulo: str,
    plataforma: str,
    genero: str,
    ano_lancamento: int
):
    jogo = Jogo(
        titulo=titulo,
        plataforma=plataforma,
        genero=genero,
        ano_lancamento=ano_lancamento
    )

    db.add(jogo)
    db.commit()
    db.refresh(jogo)

    return jogo


def get_all_jogos(
    db: Session,
    limit: int = 10,
    offset: int = 0,
    plataforma: str | None = None,
    disponivel: bool | None = None
):
    query = db.query(Jogo)

    if plataforma:
        query = query.filter(
            Jogo.plataforma == plataforma
        )

    if disponivel is not None:
        query = query.filter(
            Jogo.disponivel == disponivel
        )

    return query.offset(offset).limit(limit).all()


def get_jogo_by_id(
    db: Session,
    jogo_id: int
):
    return db.query(Jogo).filter(
        Jogo.id == jogo_id
    ).first()


def get_jogo_disponivel(
    db: Session,
    jogo_id: int
):
    return db.query(Jogo).filter(
        Jogo.id == jogo_id,
        Jogo.disponivel == True
    ).first()