from fastapi import APIRouter, Depends  
from sqlmodel import Session  
from app.schemas.estoque import EstoqueCreate, EstoqueRead  
from app.crud.estoque import create_estoque, get_estoques  
from app.database import get_session  

router = APIRouter()  

@router.post("/estoques/", response_model=EstoqueRead)  
def create_estoque_endpoint(estoque: EstoqueCreate, session: Session = Depends(get_session)):  
    return create_estoque(session, estoque)  

@router.get("/estoques/", response_model=List[EstoqueRead])  
def read_estoques(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):  
    return get_estoques(session, skip=skip, limit=limit)