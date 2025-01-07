from sqlmodel import SQLModel, Field
from datetime import date

class Remedio(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    descricao: str
    tarja: str
    preco: float
    validade: date
