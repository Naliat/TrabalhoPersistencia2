from fastapi import APIRouter, Depends, HTTPException  
from sqlmodel import Session  
from app.schemas.remedio import RemedioCreate, RemedioRead  
from app.crud.remedio import create_remedio, get_remedios  
from app.database import get_session  

router = APIRouter()  

@router.post("/remedios/", response_model=RemedioRead)  
def create_remedio_endpoint(remedio: RemedioCreate, session: Session = Depends(get_session)):  
    return create_remedio(session, remedio)  

@router.get("/remedios/", response_model=List[RemedioRead])  
def read_remedios(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):  
    return get_remedios(session, skip=skip, limit=limit)