from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.jogo import (
    JogoCreate,
    JogoResponse
)
from app.services.jogo_service import (
    criar_jogo,
    listar_jogos,
    buscar_jogo_por_id
)

router = APIRouter(
    prefix="/jogos",
    tags=["Jogos"]
)


@router.post("/", response_model=JogoResponse)
def criar(
    jogo: JogoCreate,
    db: Session = Depends(get_db)
):
    return criar_jogo(
        db=db,
        titulo=jogo.titulo,
        plataforma=jogo.plataforma,
        genero=jogo.genero,
        ano_lancamento=jogo.ano_lancamento
    )


@router.get("/", response_model=list[JogoResponse])
def listar(
    limit: int = 10,
    offset: int = 0,
    plataforma: str | None = None,
    disponivel: bool | None = None,
    db: Session = Depends(get_db)
):
    return listar_jogos(
        db=db,
        limit=limit,
        offset=offset,
        plataforma=plataforma,
        disponivel=disponivel
    )


@router.get("/{jogo_id}", response_model=JogoResponse)
def buscar(
    jogo_id: int,
    db: Session = Depends(get_db)
):
    return buscar_jogo_por_id(
        db,
        jogo_id
    )