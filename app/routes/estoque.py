from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.estoque import Estoque, EstoqueCreate
from app.crud.estoque import create_estoque, get_estoques
from app.db import get_db

router = APIRouter()

@router.post("/", response_model=Estoque)
def create(estoque: EstoqueCreate, db: Session = Depends(get_db)):
    return create_estoque(db=db, estoque=estoque)

@router.get("/", response_model=list[Estoque])
def read_estoques(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_estoques(db=db, skip=skip, limit=limit)
