from sqlalchemy.orm import Session
from app.repositories.user_repository import get_user_by_email
from app.core.security import hash_password
from app.repositories.user_repository import (
    create_user,
    get_all_users,
    get_user_by_id,
)


def criar_usuario(
    db: Session,
    nome: str,
    email: str,
    senha: str
):
    senha_hash = hash_password(senha)

    return create_user(
        db=db,
        nome=nome,
        email=email,
        senha=senha_hash
    )


def listar_usuarios(db: Session):
    return get_all_users(db)


def buscar_usuario_por_id(db: Session, user_id: int):
    return get_user_by_id(db, user_id)

def buscar_usuario_por_email(db: Session, email: str):
    return get_user_by_email(db, email)