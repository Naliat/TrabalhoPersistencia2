from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema para criação de Estoque
class EstoqueCreate(BaseModel):
    id_do_remedio: str
    quantidade: int
    data_validade: datetime
    data_entrada_estoque: datetime
    unidade_medida: str
    remedio_id: int

# Schema para atualização de Estoque (herda de EstoqueCreate)
class EstoqueUpdate(EstoqueCreate):
    pass

# Schema para criação de Fornecedor
class FornecedorCreate(BaseModel):
    nome_fornecedor: str
    contato: str
    endereco: str
    tipo_produto: str

# Schema para atualização de Fornecedor (herda de FornecedorCreate)
class FornecedorUpdate(FornecedorCreate):
    pass

# Schema para criação de Remédio
class RemedioCreate(BaseModel):
    nome: str
    tarja: str
    preco: float
    validade: datetime
    fornecedor_nome: str  # Nome do fornecedor
    fornecedor_id: int  # ID do fornecedor

# Schema para atualização de Remédio (herda de RemedioCreate)
class RemedioUpdate(RemedioCreate):
    pass
