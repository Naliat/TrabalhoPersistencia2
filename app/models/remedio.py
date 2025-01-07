# app/models/remedio.py
from sqlmodel import SQLModel, Field
from datetime import datetime

class Remedio(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    tarja: str
    preco: float
    validade: datetime
