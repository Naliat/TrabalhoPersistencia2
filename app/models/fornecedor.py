from sqlmodel import SQLModel, Field
from typing import Optional

class Fornecedor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    contato: str
    endereço: str
    tipo_produto: str
