from pydantic import BaseModel
from datetime import date

class EstoqueBase(BaseModel):
    quantidade: int
    data_validade: date
    data_entrada_estoque: date
    unidade_medida: str

class EstoqueCreate(EstoqueBase):
    pass

class Estoque(EstoqueBase):
    id_do_remedio: int

    class Config:
        orm_mode = True
