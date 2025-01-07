# app/schemas/fornecedor.py
from pydantic import BaseModel

class FornecedorCreate(BaseModel):
    nome_fornecedor: str
    contato: str
    endereco: str
    tipo_produto: str
