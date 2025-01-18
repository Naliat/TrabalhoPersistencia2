from fastapi import APIRouter, HTTPException, Depends, Query
from app.models.estoque import Estoque
from app.models.remedio import Remedio
from app.database import get_session
from sqlalchemy.orm import Session
from sqlmodel import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from sqlalchemy.sql import extract


router = APIRouter()

@router.post("/estoque/", response_model=Estoque)
async def criar_estoque_view(estoque_data: dict, session: Session = Depends(get_session)):
    try:
        remedio = session.get(Remedio, estoque_data["remedio_id"])
        if not remedio:
            raise HTTPException(status_code=404, detail="Remédio não encontrado")
        
        if "data_entrada_estoque" in estoque_data:
            estoque_data["data_entrada_estoque"] = datetime.fromisoformat(
                estoque_data["data_entrada_estoque"].replace("Z", "+00:00")
            )
        if "validade" in estoque_data:
            estoque_data["validade"] = datetime.fromisoformat(
                estoque_data["validade"].replace("Z", "+00:00")
            )
    
        novo_estoque = Estoque(**estoque_data)
        session.add(novo_estoque)
        session.commit()
        session.refresh(novo_estoque)
        return novo_estoque
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail="Erro ao criar estoque: " + str(e))

@router.get("/estoques/", response_model=list[Estoque])
async def listar_estoques_view(
    remedio_id: int = Query(None, description="Filtrar pelo ID do remédio"),
    quantidade_minima: int = Query(None, description="Quantidade mínima no estoque"),
    validade_mes: int = Query(None, ge=1, le=12, description="Filtrar pelo mês da validade (1-12)"),
    validade_ano: int = Query(None, description="Filtrar pelo ano da validade"),
    session: Session = Depends(get_session)
):
    query = select(Estoque)

    if remedio_id is not None:
        query = query.where(Estoque.remedio_id == remedio_id)
    if quantidade_minima is not None:
        query = query.where(Estoque.quantidade >= quantidade_minima)
    if validade_mes is not None and validade_ano is not None:
        query = query.where(
            extract("month", Estoque.validade) == validade_mes,
            extract("year", Estoque.validade) == validade_ano
        )
    elif validade_mes is not None:
        query = query.where(extract("month", Estoque.validade) == validade_mes)
    elif validade_ano is not None:
        query = query.where(extract("year", Estoque.validade) == validade_ano)
    
    try:
        estoques = session.exec(query).all()
        if not estoques:
            raise HTTPException(status_code=404, detail="Nenhum estoque encontrado com os critérios fornecidos")
        return estoques
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail="Erro ao buscar estoques: " + str(e))

@router.get("/estoque/{estoque_id}", response_model=Estoque)
async def obter_estoque_view(estoque_id: int, session: Session = Depends(get_session)):
    estoque = session.get(Estoque, estoque_id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque

@router.put("/estoque/{estoque_id}", response_model=Estoque)
async def atualizar_estoque_view(estoque_id: int, estoque_data: dict, session: Session = Depends(get_session)):
    try:
        estoque = session.get(Estoque, estoque_id)
        if not estoque:
            raise HTTPException(status_code=404, detail="Estoque não encontrado")
        
        for key, value in estoque_data.items():
            setattr(estoque, key, value)
            
        estoque.updated_at = datetime.now(timezone.utc)
        
        session.commit()
        session.refresh(estoque)
        return estoque
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail="Erro ao atualizar estoque: " + str(e))

@router.delete("/estoque/{estoque_id}", response_model=dict)
async def deletar_estoque_view(estoque_id: int, session: Session = Depends(get_session)):
    try:
        estoque = session.get(Estoque, estoque_id)
        if not estoque:
            raise HTTPException(status_code=404, detail="Estoque não encontrado")
        
        session.delete(estoque)
        session.commit()
        return {"detail": "Estoque deletado com sucesso"}
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail="Erro ao deletar estoque: " + str(e))
