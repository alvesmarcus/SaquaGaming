from app.core.security import (
    hash_password,
    verify_password
)


def test_hash_password():
    senha = "123456"

    senha_hash = hash_password(senha)

    assert senha_hash != senha


def test_verify_password():
    senha = "123456"

    senha_hash = hash_password(senha)

    assert verify_password(
        senha,
        senha_hash
    )