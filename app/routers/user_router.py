from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    criar_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def criar(user: UserCreate, db: Session = Depends(get_db)):
    return criar_usuario(
        db=db,
        nome=user.nome,
        email=user.email,
        senha=user.senha
    )


@router.get("/", response_model=list[UserResponse])
def listar(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return listar_usuarios(db)


@router.get("/{user_id}", response_model=UserResponse)
def buscar(user_id: int, db: Session = Depends(get_db)):
    return buscar_usuario_por_id(db, user_id)