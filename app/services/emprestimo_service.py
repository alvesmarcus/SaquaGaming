from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.emprestimo_repository import (
    create_emprestimo,
    get_all_emprestimos,
    get_emprestimo_by_id,
    get_emprestimo_ativo
)

from app.repositories.jogo_repository import (
    get_jogo_disponivel,
    get_jogo_by_id
)

def criar_emprestimo(
    db: Session,
    usuario_id: int,
    jogo_id: int
):
    jogo = get_jogo_disponivel(
        db,
        jogo_id
    )

    if not jogo:
        raise HTTPException(
            status_code=400,
            detail="Jogo indisponível"
        )

    emprestimo = create_emprestimo(
        db=db,
        usuario_id=usuario_id,
        jogo_id=jogo_id
    )

    jogo.disponivel = False

    db.commit()

    return emprestimo


def listar_emprestimos(db: Session):
    return get_all_emprestimos(db)


def buscar_emprestimo_por_id(
    db: Session,
    emprestimo_id: int
):
    return get_emprestimo_by_id(
        db,
        emprestimo_id
    )

def devolver_jogo(
    db: Session,
    emprestimo_id: int
):
    emprestimo = get_emprestimo_ativo(
        db,
        emprestimo_id
    )

    if not emprestimo:
        raise HTTPException(
            status_code=404,
            detail="Empréstimo não encontrado"
        )

    jogo = get_jogo_by_id(
        db,
        emprestimo.jogo_id
    )

    emprestimo.devolvido = True
    emprestimo.data_devolucao = datetime.utcnow()

    jogo.disponivel = True

    db.commit()

    return emprestimo