from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.remedio import Remedio
from app.database import get_session
from app.models.fornecedor import Fornecedor
from pydantic import BaseModel
from datetime import datetime, timezone
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

class RemedioCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    validade: str  # Deve ser no formato "YYYY-MM-DD"
    fornecedor_id: int


@router.post("/remedios/", response_model=Remedio)
def add_remedio(remedio: RemedioCreate, session: Session = Depends(get_session)):
    fornecedor = session.get(Fornecedor, remedio.fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")

    novo_remedio = Remedio(
        nome=remedio.nome,
        descricao=remedio.descricao,
        preco=remedio.preco,
        validade=remedio.validade,
        fornecedor_id=remedio.fornecedor_id,
    )
    session.add(novo_remedio)
    session.commit()
    session.refresh(novo_remedio)
    return novo_remedio


@router.get("/remedios/", response_model=list[Remedio])
async def listar_remedios_view(session: Session = Depends(get_session)):
    return session.exec(select(Remedio)).all()


@router.get("/remedio/{remedio_id}", response_model=Remedio)
async def obter_remedio_view(remedio_id: int, session: Session = Depends(get_session)):
    remedio = session.get(Remedio, remedio_id)
    if not remedio:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    return remedio


@router.get("/remedios/busca/", response_model=list[Remedio])
async def buscar_remedios_view(nome: str, session: Session = Depends(get_session)):
    remedios = session.exec(select(Remedio).where(Remedio.nome.contains(nome))).all()
    return remedios


@router.get("/remedios/validade/", response_model=list[Remedio])
async def listar_remedios_validade_view(
    ano: int, session: Session = Depends(get_session)
):
    remedios = session.exec(
        select(Remedio).where(
            # Converter a validade para datetime para filtrar pelo ano
            Remedio.validade.like(f"{ano}-%")
        )
    ).all()
    return remedios


@router.get("/fornecedor/{fornecedor_id}/remedios/", response_model=list[Remedio])
async def listar_remedios_por_fornecedor_view(
    fornecedor_id: int, session: Session = Depends(get_session)
):
    remedios = session.exec(
        select(Remedio).where(Remedio.fornecedor_id == fornecedor_id)
    ).all()
    return remedios

@router.put("/remedio/{remedio_id}", response_model=Remedio)
async def atualizar_remedio_view(remedio_id: int, remedio_data: dict, session: Session = Depends(get_session)):
    try:
        remedio = session.get(Remedio, remedio_id)
        if not remedio:
            raise HTTPException(status_code=404, detail="Remédio não encontrado")
        
        # Atualizar os campos
        for key, value in remedio_data.items():
            setattr(remedio, key, value)

        remedio.updated_at = datetime.now(timezone.utc)
        
        session.commit()
        session.refresh(remedio)
        return remedio
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/remedio/{remedio_id}", response_model=dict)
async def deletar_remedio_view(remedio_id: int, session: Session = Depends(get_session)):
    try:
        remedio = session.get(Remedio, remedio_id)
        if not remedio:
            raise HTTPException(status_code=404, detail="Remédio não encontrado")
        
        session.delete(remedio)
        session.commit()
        return {"detail": "Remédio deletado com sucesso"}
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
