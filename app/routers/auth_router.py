from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import verify_password, create_access_token
from app.core.database import get_db
from app.schemas.auth import LoginRequest
from app.services.user_service import buscar_usuario_por_email

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(login: LoginRequest, db: Session = Depends(get_db)):
    usuario = buscar_usuario_por_email(db, login.email)

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    if not verify_password(login.senha, usuario.senha):
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    token = create_access_token(
    data={
        "sub": usuario.email
    }
)

    return {
    "access_token": token,
    "token_type": "bearer"
    }