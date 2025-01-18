from datetime import datetime, timezone, date
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .fornecedor import Fornecedor
    from .estoque import Estoque

class RemedioBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    validade: date  
    preco: float
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Remedio(RemedioBase, table=True):
    fornecedor_id: int = Field(foreign_key="fornecedor.id")
    fornecedor: "Fornecedor" = Relationship(back_populates="remedios")
    estoques: List["Estoque"] = Relationship(back_populates="remedio")