from app.models.remedio import Remedio
from app.schemas.remedio import RemedioCreate
from sqlmodel import Session, select
from app.config import engine

# Função para criar um novo remédio
def criar_remedio(remedio: RemedioCreate):
    with Session(engine) as session:
        novo_remedio = Remedio(**remedio.dict())
        session.add(novo_remedio)
        session.commit()

# Função para obter um remédio pelo ID
def obter_remedio_por_id(remedio_id: int):
    with Session(engine) as session:
        remedio = session.query(Remedio).filter(Remedio.id == remedio_id).first()
    return remedio

# Função para listar todos os remédios
def listar_remedios():
    with Session(engine) as session:
        return session.query(Remedio).all()

# Função para listar os remédios por fornecedor
def listar_remedios_por_fornecedor(fornecedor_id: int):
    with Session(engine) as session:
        return session.query(Remedio).filter(Remedio.fornecedor_id == fornecedor_id).all()

# Função para buscar remédios pelo nome
def buscar_remedios_por_nome(nome: str):
    with Session(engine) as session:
        return session.query(Remedio).filter(Remedio.nome.ilike(f"%{nome}%")).all()

# Função para listar remédios por ano de validade
def listar_remedios_por_ano(ano: int):
    with Session(engine) as session:
        return session.query(Remedio).filter(Remedio.validade.year == ano).all()

# Função para contar a quantidade de remédios
def contar_remedios():
    with Session(engine) as session:
        return session.query(Remedio).count()

# Função para listar remédios ordenados por algum atributo
def listar_remedios_ordenados(ordenar_por: str = "preco", ordem: str = "asc"):
    with Session(engine) as session:
        if ordem == "asc":
            return session.query(Remedio).order_by(getattr(Remedio, ordenar_por).asc()).all()
        else:
            return session.query(Remedio).order_by(getattr(Remedio, ordenar_por).desc()).all()

# Função para listar remédios com fornecedor
def listar_remedios_com_fornecedor(preco_max: float = 100.0):
    from app.models.fornecedor import Fornecedor
    with Session(engine) as session:
        resultado = session.query(Remedio, Fornecedor).join(Fornecedor).filter(Remedio.preco <= preco_max).all()
    return [{"remedio": r[0], "fornecedor": r[1]} for r in resultado]

# Função para atualizar um remédio
def atualizar_remedio(remedio_id: int, remedio: RemedioCreate):
    with Session(engine) as session:
        # Buscar o remédio pelo ID
        remedio_atualizar = session.query(Remedio).filter(Remedio.id == remedio_id).first()
        if remedio_atualizar:
            # Atualizar os campos do remédio
            remedio_atualizar.nome = remedio.nome
            remedio_atualizar.tarja = remedio.tarja
            remedio_atualizar.preco = remedio.preco
            remedio_atualizar.validade = remedio.validade
            # Commit para salvar as alterações
            session.commit()
            return remedio_atualizar
        else:
            return None

# Função para apagar um remédio
def apagar_remedio(remedio_id: int):
    with Session(engine) as session:
        # Buscar o remédio pelo ID
        remedio = session.query(Remedio).filter(Remedio.id == remedio_id).first()
        if remedio:
            session.delete(remedio)
            session.commit()
            return remedio
        else:
            return None
