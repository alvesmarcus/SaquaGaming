from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.emprestimo import (
    EmprestimoCreate,
    EmprestimoResponse
)

from app.services.emprestimo_service import (
    criar_emprestimo,
    listar_emprestimos,
    buscar_emprestimo_por_id,
    devolver_jogo
)

router = APIRouter(
    prefix="/emprestimos",
    tags=["Emprestimos"]
)


@router.post("/", response_model=EmprestimoResponse)
def criar(
    emprestimo: EmprestimoCreate,
    db: Session = Depends(get_db)
):
    return criar_emprestimo(
        db=db,
        usuario_id=emprestimo.usuario_id,
        jogo_id=emprestimo.jogo_id
    )


@router.get("/", response_model=list[EmprestimoResponse])
def listar(
    db: Session = Depends(get_db)
):
    return listar_emprestimos(db)


@router.get("/{emprestimo_id}", response_model=EmprestimoResponse)
def buscar(
    emprestimo_id: int,
    db: Session = Depends(get_db)
):
    return buscar_emprestimo_por_id(
        db,
        emprestimo_id
    )

@router.post("/{emprestimo_id}/devolver")
def devolver(
    emprestimo_id: int,
    db: Session = Depends(get_db)
):
    return devolver_jogo(
        db,
        emprestimo_id
    )