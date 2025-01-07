from typing import List, Optional  
from sqlmodel import Session  
from app.models.estoque import Estoque  

def create_estoque(session: Session, estoque: Estoque) -> Estoque:  
    session.add(estoque)  
    session.commit()  
    session.refresh(estoque)  
    return estoque  

def get_estoques(session: Session, skip: int = 0, limit: int = 10) -> List[Estoque]:  
    return session.query(Estoque).offset(skip).limit(limit).all()  

def get_estoque(session: Session, estoque_id: int) -> Optional[Estoque]:  
    return session.get(Estoque, estoque_id)