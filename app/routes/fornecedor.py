from fastapi import APIRouter, Depends  
from sqlmodel import Session  
from app.schemas.fornecedor import FornecedorCreate, FornecedorRead  
from app.crud.fornecedor import create_fornecedor, get_fornecedores  
from app.database import get_session  

router = APIRouter()  

@router.post("/fornecedores/", response_model=FornecedorRead)  
def create_fornecedor_endpoint(fornecedor: FornecedorCreate, session: Session = Depends(get_session)):  
    return create_fornecedor(session, fornecedor)  

@router.get("/fornecedores/", response_model=List[FornecedorRead])  
def read_fornecedores(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):  
    return get_fornecedores(session, skip=skip, limit=limit)