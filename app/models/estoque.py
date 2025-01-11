# app/models/estoque.py
from sqlmodel import Field, SQLModel
from datetime import date

class Estoque(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_do_remedio: str
    quantidade: int
    data_validade: date
    data_entrada_estoque: date 
    unidade_medida: str
