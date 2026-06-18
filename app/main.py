from fastapi import FastAPI
from fastapi import HTTPException

from app.core.exceptions import http_exception_handler

from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router
from app.routers.jogo_router import router as jogo_router
from app.routers.emprestimo_router import router as emprestimo_router


app = FastAPI(
    title="SaquaGaming API",
    description="API para gerenciamento de empréstimos de jogos da cidade de Saquarema",
    version="1.0.0"
)

# ADICIONE ISSO
app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(jogo_router)
app.include_router(emprestimo_router)


@app.get("/")
def home():
    return {
        "message": "Bem-vindo ao SaquaGaming!"
    }