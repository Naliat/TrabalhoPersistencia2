from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Remédio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    tarja: str
    preço: float
    validade: date
