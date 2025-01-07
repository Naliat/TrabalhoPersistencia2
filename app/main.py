from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from app.config import settings
from app.routes import remédio, fornecedor, estoque

app = FastAPI()

engine = create_engine(settings.database_url)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(remédio.router)
app.include_router(fornecedor.router)
app.include_router(estoque.router)
