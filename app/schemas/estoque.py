# app/schemas/estoque.py
from pydantic import BaseModel
from datetime import date

class EstoqueCreate(BaseModel):
    id_do_remedio: str
    quantidade: int
    data_validade: date
    data_entrada_estoque: date
    unidade_medida: str