from app.schemas.user import UserCreate
import pytest


def test_nome_valido():
    user = UserCreate(
        nome="Marcus",
        email="marcus@email.com",
        senha="123456"
    )

    assert user.nome == "Marcus"


def test_nome_invalido():
    with pytest.raises(ValueError):
        UserCreate(
            nome="Ma",
            email="marcus@email.com",
            senha="123456"
        )


def test_senha_valida():
    user = UserCreate(
        nome="Marcus",
        email="marcus@email.com",
        senha="123456"
    )

    assert user.senha == "123456"


def test_senha_invalida():
    with pytest.raises(ValueError):
        UserCreate(
            nome="Marcus",
            email="marcus@email.com",
            senha="123"
        )