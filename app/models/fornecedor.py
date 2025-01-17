from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.remedio import Remedio
class Fornecedor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    cnpj: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None

    remedios: List["Remedio"] = Relationship(back_populates="fornecedor")
