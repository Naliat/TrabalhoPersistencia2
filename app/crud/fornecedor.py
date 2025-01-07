from typing import List, Optional  
from sqlmodel import Session  
from app.models.fornecedor import Fornecedor  

def create_fornecedor(session: Session, fornecedor: Fornecedor) -> Fornecedor:  
    session.add(fornecedor)  
    session.commit()  
    session.refresh(fornecedor)  
    return fornecedor  

def get_fornecedores(session: Session, skip: int = 0, limit: int = 10) -> List[Fornecedor]:  
    return session.query(Fornecedor).offset(skip).limit(limit).all()  

def get_fornecedor(session: Session, fornecedor_id: int) -> Optional[Fornecedor]:  
    return session.get(Fornecedor, fornecedor_id)