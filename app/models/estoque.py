from sqlmodel import SQLModel, Field
from datetime import date

class Estoque(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_do_remedio: int = Field(foreign_key="remedio.id")
    quantidade: int
    data_validade: date
    data_entrada_estoque: date
    unidade_medida: str
