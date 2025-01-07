from sqlmodel import SQLModel, Field

class Fornecedor(SQLModel, table=True):
    ID_Fornecedor: int = Field(default=None, primary_key=True)
    nome_fornecedor: str
    contato: str
    endereco: str
    tipo_produto: str
