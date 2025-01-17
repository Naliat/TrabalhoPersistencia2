from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.remedio import Remedio


class EstoqueBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    quantidade: int
    data_entrada_estoque: datetime = Field(default_factory=datetime.utcnow)
    validade: datetime


class Estoque(EstoqueBase, table=True):
    remedio_id: int = Field(foreign_key="remedio.id")
    remedio: "Remedio" = Relationship(back_populates="estoques")


class EstoqueBaseWithRemedio(EstoqueBase):
    remedio: Optional["Remedio"]
