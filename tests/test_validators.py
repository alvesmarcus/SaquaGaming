from app.schemas.jogo import JogoCreate
import pytest


def test_titulo_valido():
    jogo = JogoCreate(
        titulo="GTA V",
        plataforma="PC",
        genero="Ação",
        ano_lancamento=2013
    )

    assert jogo.titulo == "GTA V"


def test_titulo_invalido():
    with pytest.raises(ValueError):
        JogoCreate(
            titulo="AB",
            plataforma="PC",
            genero="Ação",
            ano_lancamento=2013
        )


def test_ano_valido():
    jogo = JogoCreate(
        titulo="Minecraft",
        plataforma="PC",
        genero="Sandbox",
        ano_lancamento=2011
    )

    assert jogo.ano_lancamento == 2011


def test_ano_invalido():
    with pytest.raises(ValueError):
        JogoCreate(
            titulo="Mario",
            plataforma="Nintendo",
            genero="Plataforma",
            ano_lancamento=1940
        )