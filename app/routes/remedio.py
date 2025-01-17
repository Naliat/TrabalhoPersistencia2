from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.remedio import Remedio
from app.database import get_session
from app.models.fornecedor import Fornecedor
from pydantic import BaseModel
from datetime import datetime, date, timezone
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

router = APIRouter()

class RemedioCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    validade: date
    fornecedor_id: int

    class Config:
        orm_mode = True


@router.post("/remedios/", response_model=dict)
def add_remedios(remedios: list[RemedioCreate] | RemedioCreate, session: Session = Depends(get_session)):
    # Verifica se remédios é uma lista. Se não, coloca em uma lista.
    if not isinstance(remedios, list):
        remedios = [remedios]

    fornecedores = {f.id: f for f in session.exec(select(Fornecedor)).all()}
    novos_remedios = []

    for remedio in remedios:
        fornecedor = fornecedores.get(remedio.fornecedor_id)
        if not fornecedor:
            raise HTTPException(status_code=404, detail=f"Fornecedor com ID {remedio.fornecedor_id} não encontrado")

        novo_remedio = Remedio(
            nome=remedio.nome,
            descricao=remedio.descricao,
            preco=remedio.preco,
            validade=remedio.validade,
            fornecedor_id=remedio.fornecedor_id,
        )
        session.add(novo_remedio)
        novos_remedios.append(novo_remedio)

    try:
        session.commit()  # Commit dentro do try-except para pegar possíveis falhas
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail="Erro ao salvar os remédios: " + str(e))

    # Mensagem de sucesso
    return {"detail": f"{len(novos_remedios)} remédios adicionados com sucesso", "remedios": novos_remedios}


@router.get("/remedios/", response_model=list[Remedio])
async def listar_remedios_view(session: Session = Depends(get_session)):
    return session.exec(select(Remedio)).all()  # Listar todos os remédios


@router.get("/remedio/{remedio_id}", response_model=Remedio)
async def obter_remedio_view(remedio_id: int, session: Session = Depends(get_session)):
    remedio = session.get(Remedio, remedio_id)
    if not remedio:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    return remedio  # Retornar o remédio específico


@router.get("/remedios/busca/", response_model=list[Remedio])
async def buscar_remedios_view(nome: str, session: Session = Depends(get_session)):
    remedios = session.exec(select(Remedio).where(Remedio.nome.contains(nome))).all()
    return remedios  # Buscar remédios pelo nome


@router.get("/remedios/validade/")
async def listar_remedios_validade_view(ano: int, db: Session = Depends(get_session)):
    try:
        # Ajuste na consulta para extrair corretamente o ano da validade
        remedios = db.query(Remedio).filter(func.extract('year', Remedio.validade) == ano).all()
        return remedios
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail="Erro ao consultar os remédios: " + str(e))


@router.get("/fornecedor/{fornecedor_id}/remedios/", response_model=list[Remedio])
async def listar_remedios_por_fornecedor_view(
    fornecedor_id: int, session: Session = Depends(get_session)
):
    try:
        remedios = session.exec(
            select(Remedio).where(Remedio.fornecedor_id == fornecedor_id)
        ).all()
        return remedios  # Listar remédios de um fornecedor específico
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail="Erro ao listar os remédios: " + str(e))

@router.get("/remedios/validade-preco/", response_model=list[Remedio])
def busca_remedios_validade_preco(
    preco_min: float = 0.0, 
    preco_max: float = float("inf"),
    validade_min: date = date.today(), 
    validade_max: date = date.today(), 
    session: Session = Depends(get_session)
):
    return session.exec(
        select(Remedio).where(
            Remedio.preco.between(preco_min, preco_max),
            Remedio.validade.between(validade_min, validade_max)
        )
    ).all()



@router.put("/remedio/{remedio_id}", response_model=Remedio)
async def atualizar_remedio_view(remedio_id: int, remedio_data: dict, session: Session = Depends(get_session)):
    try:
        remedio = session.get(Remedio, remedio_id)
        if not remedio:
            raise HTTPException(status_code=404, detail="Remédio não encontrado")
        
        # Atualizar os campos do remédio
        for key, value in remedio_data.items():
            if value is not None:  # Verificar se o valor não é None antes de atualizar
                if key == "validade" and isinstance(value, str):
                    # Converter a string para um objeto date
                    value = datetime.strptime(value, "%Y-%m-%d").date()
                setattr(remedio, key, value)

        remedio.updated_at = datetime.now(timezone.utc)  # Atualizar a data de modificação
        
        session.commit()  # Confirmar a transação
        session.refresh(remedio)  # Atualizar o objeto com dados mais recentes
        return remedio  # Retornar o remédio atualizado
    except SQLAlchemyError as e:
        session.rollback()  # Reverter a transação em caso de erro
        raise HTTPException(status_code=400, detail="Erro ao atualizar o remédio: " + str(e))  # Retornar erro ao usuário
@router.delete("/remedio/{remedio_id}", response_model=dict)
async def deletar_remedio_view(remedio_id: int, session: Session = Depends(get_session)):
    try:
        remedio = session.get(Remedio, remedio_id)
        if not remedio:
            raise HTTPException(status_code=404, detail="Remédio não encontrado")
        
        session.delete(remedio)  # Deletar o remédio
        session.commit()  # Confirmar a transação
        return {"detail": "Remédio deletado com sucesso"}  # Confirmar exclusão
    except SQLAlchemyError as e:
        session.rollback()  # Reverter a transação em caso de erro
        raise HTTPException(status_code=400, detail="Erro ao deletar o remédio: " + str(e))  # Retornar erro ao usuário