from sqlmodel import Session
from app.models.fornecedor import Fornecedor

def create_fornecedor(db: Session, fornecedor: Fornecedor):
    db.add(fornecedor)
    db.commit()
    db.refresh(fornecedor)
    return fornecedor

def get_fornecedores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Fornecedor).offset(skip).limit(limit).all()
