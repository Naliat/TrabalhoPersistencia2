from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.fornecedor import Fornecedor, FornecedorCreate
from app.crud.fornecedor import create_fornecedor, get_fornecedores
from app.db import get_db

router = APIRouter()

@router.post("/", response_model=Fornecedor)
def create(fornecedor: FornecedorCreate, db: Session = Depends(get_db)):
    return create_fornecedor(db=db, fornecedor=fornecedor)

@router.get("/", response_model=list[Fornecedor])
def read_fornecedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_fornecedores(db=db, skip=skip, limit=limit)
