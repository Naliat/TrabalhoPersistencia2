from app.models.fornecedor import Fornecedor
from app.schemas.fornecedor import FornecedorCreate
from sqlmodel import Session
from app.config import engine

# Função para criar um novo fornecedor
def criar_fornecedor(fornecedor: FornecedorCreate):
    with Session(engine) as session:
        novo_fornecedor = Fornecedor(**fornecedor.dict())
        session.add(novo_fornecedor)
        session.commit()

# Função para obter um fornecedor pelo ID
def obter_fornecedor_por_id(fornecedor_id: int):
    with Session(engine) as session:
        fornecedor = session.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
    return fornecedor

# Função para listar todos os fornecedores
def listar_fornecedores():
    with Session(engine) as session:
        return session.query(Fornecedor).all()

# Função para contar a quantidade de fornecedores
def contar_fornecedores():
    with Session(engine) as session:
        return session.query(Fornecedor).count()

# Função para atualizar um fornecedor
def atualizar_fornecedor(fornecedor_id: int, fornecedor: FornecedorCreate):
    with Session(engine) as session:
        # Buscar o fornecedor pelo ID
        fornecedor_atualizar = session.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
        if fornecedor_atualizar:
            # Atualizar os campos do fornecedor
            fornecedor_atualizar.nome_fornecedor = fornecedor.nome_fornecedor
            fornecedor_atualizar.contato = fornecedor.contato
            fornecedor_atualizar.endereco = fornecedor.endereco
            fornecedor_atualizar.tipo_produto = fornecedor.tipo_produto
            # Commit para salvar as alterações
            session.commit()
            return fornecedor_atualizar
        else:
            return None

# Função para apagar um fornecedor
def apagar_fornecedor(fornecedor_id: int):
    with Session(engine) as session:
        # Buscar o fornecedor pelo ID
        fornecedor = session.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
        if fornecedor:
            session.delete(fornecedor)
            session.commit()
            return fornecedor
        else:
            return None
