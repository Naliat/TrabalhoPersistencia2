from pydantic import BaseModel

class RemedioCreate(BaseModel):
    nome: str
    tarja: str
    preco: float
    validade: str
    fornecedor_id: int
