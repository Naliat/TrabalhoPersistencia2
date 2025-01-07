from fastapi import FastAPI
from app.routes import remedio, fornecedor, estoque

app = FastAPI(title="Gerenciador de Remédios")

# Registrar as rotas
app.include_router(remedio.router, prefix="/remedios", tags=["Remédios"])
app.include_router(fornecedor.router, prefix="/fornecedores", tags=["Fornecedores"])
app.include_router(estoque.router, prefix="/estoques", tags=["Estoques"])

@app.get("/")
def root():
    return {"message": "Bem-vindo ao Gerenciador de Remédios!"}
