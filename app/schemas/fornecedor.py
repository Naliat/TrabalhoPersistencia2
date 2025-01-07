from pydantic import BaseModel

class FornecedorBase(BaseModel):
    nome_fornecedor: str
    contato: str
    endereco: str
    tipo_produto: str

class FornecedorCreate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    ID_Fornecedor: int

    class Config:
        orm_mode = True
