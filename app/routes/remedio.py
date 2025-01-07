from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.remedio import Remedio, RemedioCreate
from app.crud.remedio import create_remedio, get_remedios, get_remedio_by_id
from app.db import get_db


router = APIRouter()

@router.post("/", response_model=Remedio)
def create(remedio: RemedioCreate, db: Session = Depends(get_db)):
    return create_remedio(db=db, remedio=remedio)

@router.get("/", response_model=list[Remedio])
def read_remedios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_remedios(db=db, skip=skip, limit=limit)

@router.get("/{remedio_id}", response_model=Remedio)
def read_remedio(remedio_id: int, db: Session = Depends(get_db)):
    db_remedio = get_remedio_by_id(db=db, remedio_id=remedio_id)
    if db_remedio is None:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    return db_remedio
