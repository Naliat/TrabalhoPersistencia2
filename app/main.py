from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine
from sqlmodel import SQLModel
from app.routes.fornecedor import router as fornecedor_router
from app.routes.remedio import router as remedio_router
from app.routes.estoque import router as estoque_router


# Função para criação do banco de dados e tabelas
def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)


# Configurações de inicialização com ciclo de vida assíncrono
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


# Inicializa o aplicativo FastAPI
app = FastAPI(lifespan=lifespan)

# Inclui as rotas para os endpoints
app.include_router(fornecedor_router)  # Incluindo o router de fornecedor
app.include_router(remedio_router)  # Incluindo o router de remédio
app.include_router(estoque_router)  # Incluindo o router de estoque


# Rota Home de boas-vindas
@app.get("/")
def read_home():
    return {"message": "Bem-vindo à API de gerenciamento de remédios!"}
