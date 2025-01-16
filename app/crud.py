from datetime import datetime
from sqlmodel import Session, select
from app.models import Estoque, Fornecedor, Remedio
from app.config import engine
from sqlalchemy.exc import SQLAlchemyError

# Função para obter a sessão do banco de dados
def get_session():
    try:
        session = Session(engine)
        return session
    except SQLAlchemyError as e:
        print(f"Erro ao criar a sessão: {e}")
        return None

# Funções CRUD para Estoque
def criar_estoque(session: Session, estoque_data: dict):
    try:
        novo_estoque = Estoque(**estoque_data)
        session.add(novo_estoque)
        session.commit()
        session.refresh(novo_estoque)
        return novo_estoque
    except SQLAlchemyError as e:
        print(f"Erro ao criar estoque: {e}")
        session.rollback()
        return None

def obter_estoque_por_id(session: Session, estoque_id: int):
    return session.exec(select(Estoque).where(Estoque.id == estoque_id)).first()

def listar_estoques_por_remedio(session: Session, remedio_id: int):
    return session.exec(select(Estoque).where(Estoque.remedio_id == remedio_id)).all()

def listar_estoques_por_data(session: Session, data: datetime):
    return session.exec(select(Estoque).where(Estoque.data_entrada_estoque >= data)).all()

def contar_estoque(session: Session):
    return session.exec(select(Estoque)).count()

def atualizar_estoque(session: Session, estoque_id: int, estoque_data: dict):
    estoque = session.exec(select(Estoque).where(Estoque.id == estoque_id)).first()
    if estoque:
        for key, value in estoque_data.items():
            setattr(estoque, key, value)
        session.commit()
        session.refresh(estoque)
        return estoque
    return None

def apagar_estoque(session: Session, estoque_id: int):
    estoque = session.exec(select(Estoque).where(Estoque.id == estoque_id)).first()
    if estoque:
        session.delete(estoque)
        session.commit()
        return estoque
    return None

# Funções CRUD para Fornecedor
def criar_fornecedor(session: Session, fornecedor_data: dict):
    try:
        novo_fornecedor = Fornecedor(**fornecedor_data)
        session.add(novo_fornecedor)
        session.commit()
        session.refresh(novo_fornecedor)
        return novo_fornecedor
    except SQLAlchemyError as e:
        print(f"Erro ao criar fornecedor: {e}")
        session.rollback()
        return None

def obter_fornecedor_por_id(session: Session, fornecedor_id: int):
    return session.exec(select(Fornecedor).where(Fornecedor.id == fornecedor_id)).first()

def listar_fornecedores(session: Session):
    return session.exec(select(Fornecedor)).all()

def contar_fornecedores(session: Session):
    return session.exec(select(Fornecedor)).count()

def atualizar_fornecedor(session: Session, fornecedor_id: int, fornecedor_data: dict):
    fornecedor = session.exec(select(Fornecedor).where(Fornecedor.id == fornecedor_id)).first()
    if fornecedor:
        for key, value in fornecedor_data.items():
            setattr(fornecedor, key, value)
        session.commit()
        session.refresh(fornecedor)
        return fornecedor
    return None

def apagar_fornecedor(session: Session, fornecedor_id: int):
    fornecedor = session.exec(select(Fornecedor).where(Fornecedor.id == fornecedor_id)).first()
    if fornecedor:
        session.delete(fornecedor)
        session.commit()
        return fornecedor
    return None

# Funções CRUD para Remédio
def listar_remedios(session: Session, skip: int = 0, limit: int = 10):
    return session.exec(select(Remedio).offset(skip).limit(limit)).all()

def criar_remedio(session: Session, remedio_data: dict):
    try:
        novo_remedio = Remedio(**remedio_data)
        session.add(novo_remedio)
        session.commit()
        session.refresh(novo_remedio)
        return novo_remedio
    except SQLAlchemyError as e:
        print(f"Erro ao criar remédio: {e}")
        session.rollback()
        return None

def obter_remedio_por_id(session: Session, remedio_id: int):
    return session.exec(select(Remedio).where(Remedio.id == remedio_id)).first()

def listar_remedios_por_fornecedor(session: Session, fornecedor_id: int):
    return session.exec(select(Remedio).where(Remedio.fornecedor_id == fornecedor_id)).all()

def buscar_remedios_por_nome(session: Session, nome: str):
    return session.exec(select(Remedio).where(Remedio.nome.like(f"%{nome}%"))).all()

def listar_remedios_por_ano(session: Session, ano: int):
    return session.exec(select(Remedio).where(Remedio.validade.like(f"{ano}%"))).all()

def contar_remedios(session: Session):
    return session.exec(select(Remedio)).count()

def listar_remedios_ordenados(session: Session, ordenar_por: str = "preco", ordem: str = "asc"):
    if ordenar_por == "preco":
        return session.exec(
            select(Remedio).order_by(Remedio.preco.asc() if ordem == "asc" else Remedio.preco.desc())
        ).all()
    return session.exec(
        select(Remedio).order_by(Remedio.nome.asc() if ordem == "asc" else Remedio.nome.desc())
    ).all()

def listar_remedios_com_fornecedor(session: Session):
    return session.exec(select(Remedio, Fornecedor).join(Fornecedor)).all()
