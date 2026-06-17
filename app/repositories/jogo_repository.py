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


def get_all_jogos(db: Session):
    return db.query(Jogo).all()


def get_jogo_by_id(
    db: Session,
    jogo_id: int
):
    return db.query(Jogo).filter(
        Jogo.id == jogo_id
    ).first()