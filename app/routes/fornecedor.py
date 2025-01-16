from fastapi import APIRouter, HTTPException, Depends
from app.models.fornecedor import Fornecedor
from app.database import get_session  # Certifique-se de importar get_session
from sqlalchemy.orm import Session
from sqlmodel import select
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

# Função para criar fornecedor
@router.post("/fornecedor/", response_model=Fornecedor)
async def criar_fornecedor_view(fornecedor_data: dict, session: Session = Depends(get_session)):
    try:
        novo_fornecedor = Fornecedor(**fornecedor_data)
        session.add(novo_fornecedor)
        session.commit()
        session.refresh(novo_fornecedor)
        return novo_fornecedor
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Função para listar fornecedores
@router.get("/fornecedores/", response_model=list[Fornecedor])
async def listar_fornecedores_view(session: Session = Depends(get_session)):
    return session.exec(select(Fornecedor)).all()

# Função para obter fornecedor por ID
@router.get("/fornecedor/{fornecedor_id}", response_model=Fornecedor)
async def obter_fornecedor_view(fornecedor_id: int, session: Session = Depends(get_session)):
    fornecedor = session.get(Fornecedor, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

# Função para buscar fornecedores por nome
@router.get("/fornecedores/busca/", response_model=list[Fornecedor])
async def buscar_fornecedores_view(nome: str, session: Session = Depends(get_session)):
    fornecedores = session.exec(select(Fornecedor).where(Fornecedor.nome.contains(nome))).all()
    return fornecedores
