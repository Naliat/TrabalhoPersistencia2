from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List

# Importação condicional para evitar referência circular
if TYPE_CHECKING:
    from .fornecedor import Fornecedor
    from .estoque import Estoque  # Adicionado para resolver a relação com Estoque

# Base do modelo Remedio
class RemedioBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# Modelo completo, representando a tabela no banco
class Remedio(RemedioBase, table=True):
    fornecedor_id: int = Field(foreign_key="fornecedor.id")
    fornecedor: "Fornecedor" = Relationship(back_populates="remedios")
    estoques: List["Estoque"] = Relationship(back_populates="remedio")  # Adicionado relacionamento com Estoque

# Modelo estendido para leitura, incluindo informações do fornecedor
class RemedioBaseWithFornecedor(RemedioBase):
    fornecedor: "Fornecedor"
