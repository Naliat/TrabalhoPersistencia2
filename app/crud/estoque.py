from sqlmodel import Session
from app.models.estoque import Estoque

def create_estoque(db: Session, estoque: Estoque):
    db.add(estoque)
    db.commit()
    db.refresh(estoque)
    return estoque

def get_estoques(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Estoque).offset(skip).limit(limit).all()
