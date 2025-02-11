from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey

if TYPE_CHECKING:
    from app.models.remedio import Remedio

class EstoqueBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    quantidade: int
    data_entrada_estoque: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    validade: datetime

class Estoque(EstoqueBase, table=True):
    remedio_id: int = Field(sa_column=Column(Integer, ForeignKey('remedio.id', ondelete='CASCADE')))
    remedio: "Remedio" = Relationship(back_populates="estoques")
