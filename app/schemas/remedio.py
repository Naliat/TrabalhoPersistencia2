# app/schemas/remedio.py
from pydantic import BaseModel
from datetime import datetime

class RemedioCreate(BaseModel):
    nome: str
    preco: float
    validade: datetime
    tarja: str
    fornecedor_id: int
