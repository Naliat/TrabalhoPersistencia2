from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

# Modelo para o Estoque
class Estoque(SQLModel, table=True):
    id_estoque: Optional[int] = Field(default=None, primary_key=True)
    quantidade: int
    preco: float
    data_validade: datetime
    id_remedio: int = Field(foreign_key="remedio.id_remedio")
    id_fornecedor: int = Field(foreign_key="fornecedor.id_fornecedor")

    # Relacionamentos
    remedio: Optional["Remedio"] = Relationship(back_populates="estoques")
    fornecedor: Optional["Fornecedor"] = Relationship(back_populates="estoques")

    def __repr__(self):
        return f"<Estoque(id_estoque={self.id_estoque}, quantidade={self.quantidade}, preco={self.preco})>"

# Modelo para o Fornecedor
class Fornecedor(SQLModel, table=True):
    id_fornecedor: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    telefone: Optional[str] = None
    email: Optional[str] = None
    endereco: Optional[str] = None

    # Relacionamentos
    estoques: List[Estoque] = Relationship(back_populates="fornecedor")
    remedios: List["Remedio"] = Relationship(back_populates="fornecedor")

    def __repr__(self):
        return f"<Fornecedor(id_fornecedor={self.id_fornecedor}, nome={self.nome})>"

# Modelo para o Remédio
class Remedio(SQLModel, table=True):
    id_remedio: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: Optional[str] = None
    preco: float
    data_fabricacao: datetime
    validade: datetime
    id_fornecedor: int = Field(foreign_key="fornecedor.id_fornecedor")

    # Relacionamentos
    fornecedor: Optional[Fornecedor] = Relationship(back_populates="remedios")
    estoques: List[Estoque] = Relationship(back_populates="remedio")

    def __repr__(self):
        return f"<Remedio(id_remedio={self.id_remedio}, nome={self.nome}, preco={self.preco})>"
