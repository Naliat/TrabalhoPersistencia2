from typing import List, Optional  
from sqlmodel import Session  
from app.models.remedio import Remedio  

def create_remedio(session: Session, remedio: Remedio) -> Remedio:  
    session.add(remedio)  
    session.commit()  
    session.refresh(remedio)  
    return remedio  

def get_remedios(session: Session, skip: int = 0, limit: int = 10) -> List[Remedio]:  
    return session.query(Remedio).offset(skip).limit(limit).all()  

def get_remedio(session: Session, remedio_id: int) -> Optional[Remedio]:  
    return session.get(Remedio, remedio_id)  