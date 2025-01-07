from fastapi import FastAPI
from app.routes import remedio, fornecedor

app = FastAPI()

# Rota simples de Olá
@app.get("/")
def read_root():
    return {"message": "Olá, o servidor está funcionando!"}

# Incluindo as rotas
app.include_router(remedio.router)
app.include_router(fornecedor.router)
