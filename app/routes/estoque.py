from fastapi import APIRouter, HTTPException, Depends
from app.models.estoque import Estoque
from app.database import get_session  
from sqlalchemy.orm import Session
from sqlmodel import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

router = APIRouter()

# Função para criar estoque
@router.post("/estoque/", response_model=Estoque)
async def criar_estoque_view(estoque_data: dict, session: Session = Depends(get_session)):
    try:
        # Convertendo as strings de data para objetos datetime
        if 'data_entrada_estoque' in estoque_data:
            estoque_data['data_entrada_estoque'] = datetime.fromisoformat(estoque_data['data_entrada_estoque'].replace('Z', '+00:00'))
        if 'validade' in estoque_data:
            estoque_data['validade'] = datetime.fromisoformat(estoque_data['validade'].replace('Z', '+00:00'))
        
        novo_estoque = Estoque(**estoque_data)
        session.add(novo_estoque)
        session.commit()
        session.refresh(novo_estoque)
        return novo_estoque
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Função para listar estoques
@router.get("/estoques/", response_model=list[Estoque])
async def listar_estoques_view(session: Session = Depends(get_session)):
    return session.exec(select(Estoque)).all()

# Função para obter estoque por ID
@router.get("/estoque/{estoque_id}", response_model=Estoque)
async def obter_estoque_view(estoque_id: int, session: Session = Depends(get_session)):
    estoque = session.get(Estoque, estoque_id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque
