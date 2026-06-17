from sqlalchemy.orm import Session

from app.models.emprestimo import Emprestimo


def create_emprestimo(
    db: Session,
    usuario_id: int,
    jogo_id: int
):
    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        jogo_id=jogo_id
    )

    db.add(emprestimo)
    db.commit()
    db.refresh(emprestimo)

    return emprestimo


def get_all_emprestimos(db: Session):
    return db.query(Emprestimo).all()


def get_emprestimo_by_id(
    db: Session,
    emprestimo_id: int
):
    return db.query(Emprestimo).filter(
        Emprestimo.id == emprestimo_id
    ).first()

def get_emprestimo_ativo(
    db: Session,
    emprestimo_id: int
):
    return db.query(Emprestimo).filter(
        Emprestimo.id == emprestimo_id,
        Emprestimo.devolvido == False
    ).first()