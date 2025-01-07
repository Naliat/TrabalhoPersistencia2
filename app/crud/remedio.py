from sqlmodel import Session
from app.models.remedio import Remedio

def create_remedio(db: Session, remedio: Remedio):
    db.add(remedio)
    db.commit()
    db.refresh(remedio)
    return remedio

def get_remedios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Remedio).offset(skip).limit(limit).all()

def get_remedio_by_id(db: Session, remedio_id: int):
    return db.query(Remedio).filter(Remedio.id == remedio_id).first()
