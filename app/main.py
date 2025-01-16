from fastapi import FastAPI
from app.routes import router  # Importando o router do arquivo routes.py
from app.config import SQLALCHEMY_DATABASE_URL, engine
from sqlmodel import SQLModel

# Inicializando a aplicação FastAPI
app = FastAPI()

# Rota simples de Olá
@app.get("/")
def read_root():
    return {"message": "Olá, o servidor está funcionando!"}

# Incluindo todas as rotas definidas no router
app.include_router(router)

# Criação das tabelas no banco de dados
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(bind=engine)
