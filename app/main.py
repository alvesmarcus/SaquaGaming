from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router
from app.routers.jogo_router import router as jogo_router
app = FastAPI(
    title="SaquaGaming API",
    description="API para gerenciamento de empréstimos de jogos da cidade de Saquarema",
    version="1.0.0"
)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(jogo_router)
@app.get("/")
def home():
    return {
        "message": "Bem-vindo ao SaquaGaming!"
    }