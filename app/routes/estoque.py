from fastapi import APIRouter, HTTPException, Depends
from app.models.estoque import Estoque
from app.models.remedio import Remedio 
from app.database import get_session
from sqlalchemy.orm import Session
from sqlmodel import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone

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
async def listar_estoques_view(session: Session = Depends(get_session)):
    return session.exec(select(Estoque)).all()
 
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