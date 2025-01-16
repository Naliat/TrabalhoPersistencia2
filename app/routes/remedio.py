from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.remedio import Remedio
from app.database import get_session  # Certifique-se de importar get_session
from app.models.fornecedor import Fornecedor
from pydantic import BaseModel

router = APIRouter()

# Pydantic model para a validação da entrada de dados
class RemedioCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    validade: str
    fornecedor_id: int

@router.post("/remedios/", response_model=Remedio)
def add_remedio(remedio: RemedioCreate):
    with Session(engine) as session:
        fornecedor = session.get(Fornecedor, remedio.fornecedor_id)
        if not fornecedor:
            raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
        
        novo_remedio = Remedio(
            nome=remedio.nome,
            descricao=remedio.descricao,
            preco=remedio.preco,
            validade=remedio.validade,
            fornecedor_id=remedio.fornecedor_id
        )
        session.add(novo_remedio)
        session.commit()
        session.refresh(novo_remedio)
        return novo_remedio

# Função para listar remédios
@router.get("/remedios/", response_model=list[Remedio])
async def listar_remedios_view(session: Session = Depends(get_session)):
    return session.exec(select(Remedio)).all()

# Função para obter remédio por ID
@router.get("/remedio/{remedio_id}", response_model=Remedio)
async def obter_remedio_view(remedio_id: int, session: Session = Depends(get_session)):
    remedio = session.get(Remedio, remedio_id)
    if not remedio:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    return remedio

# Função para buscar remédios por nome
@router.get("/remedios/busca/", response_model=list[Remedio])
async def buscar_remedios_view(nome: str, session: Session = Depends(get_session)):
    remedios = session.exec(select(Remedio).where(Remedio.nome.contains(nome))).all()
    return remedios

# Função para listar remédios por validade
@router.get("/remedios/validade/", response_model=list[Remedio])
async def listar_remedios_validade_view(ano: int, session: Session = Depends(get_session)):
    remedios = session.exec(select(Remedio).where(Remedio.validade.year == ano)).all()
    return remedios

# Função para listar remédios por fornecedor
@router.get("/fornecedor/{fornecedor_id}/remedios/", response_model=list[Remedio])
async def listar_remedios_por_fornecedor_view(fornecedor_id: int, session: Session = Depends(get_session)):
    remedios = session.exec(select(Remedio).where(Remedio.fornecedor_id == fornecedor_id)).all()
    return remedios
