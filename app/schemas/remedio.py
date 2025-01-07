from pydantic import BaseModel
from datetime import date

class RemedioBase(BaseModel):
    nome: str
    tarja: str
    preco: float
    validade: date

class RemedioCreate(RemedioBase):
    pass

class Remedio(RemedioBase):
    id: int

    class Config:
        orm_mode = True
