from fastapi import APIRouter, HTTPException, Depends
from app.crud import (
    criar_estoque, obter_estoque_por_id, listar_estoques_por_remedio,
    listar_estoques_por_data, contar_estoque, atualizar_estoque, apagar_estoque,
    criar_fornecedor, obter_fornecedor_por_id, listar_fornecedores, contar_fornecedores,
    atualizar_fornecedor, apagar_fornecedor,
    listar_remedios, criar_remedio, obter_remedio_por_id, listar_remedios_por_fornecedor,
    buscar_remedios_por_nome, listar_remedios_por_ano, contar_remedios, listar_remedios_ordenados,
    listar_remedios_com_fornecedor
)
from app.models import Estoque, Fornecedor, Remedio
from app.config import engine
from sqlmodel import Session

router = APIRouter()

# Dependência para obter a sessão
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

# Rotas para Estoque
@router.post("/estoque/", response_model=Estoque)
async def criar_estoque_view(estoque_data: dict, session: Session = Depends(get_session)):
    return criar_estoque(session, estoque_data)

@router.get("/estoque/{estoque_id}", response_model=Estoque)
async def obter_estoque_view(estoque_id: int, session: Session = Depends(get_session)):
    estoque = obter_estoque_por_id(session, estoque_id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque

@router.get("/estoques/remedio/{remedio_id}", response_model=list[Estoque])
async def listar_estoques_por_remedio_view(remedio_id: int, session: Session = Depends(get_session)):
    return listar_estoques_por_remedio(session, remedio_id)

@router.get("/estoques/data/{data}", response_model=list[Estoque])
async def listar_estoques_por_data_view(data: str, session: Session = Depends(get_session)):
    return listar_estoques_por_data(session, data)

@router.get("/estoques/count", response_model=int)
async def contar_estoque_view(session: Session = Depends(get_session)):
    return contar_estoque(session)

@router.put("/estoque/{estoque_id}", response_model=Estoque)
async def atualizar_estoque_view(estoque_id: int, estoque_data: dict, session: Session = Depends(get_session)):
    estoque = atualizar_estoque(session, estoque_id, estoque_data)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque

@router.delete("/estoque/{estoque_id}", response_model=Estoque)
async def apagar_estoque_view(estoque_id: int, session: Session = Depends(get_session)):
    estoque = apagar_estoque(session, estoque_id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque

# Rotas para Fornecedor
@router.post("/fornecedor/", response_model=Fornecedor)
async def criar_fornecedor_view(fornecedor_data: dict, session: Session = Depends(get_session)):
    return criar_fornecedor(session, fornecedor_data)

@router.get("/fornecedor/{fornecedor_id}", response_model=Fornecedor)
async def obter_fornecedor_view(fornecedor_id: int, session: Session = Depends(get_session)):
    fornecedor = obter_fornecedor_por_id(session, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

@router.get("/fornecedores/", response_model=list[Fornecedor])
async def listar_fornecedores_view(session: Session = Depends(get_session)):
    return listar_fornecedores(session)

@router.get("/fornecedores/count", response_model=int)
async def contar_fornecedores_view(session: Session = Depends(get_session)):
    return contar_fornecedores(session)

@router.put("/fornecedor/{fornecedor_id}", response_model=Fornecedor)
async def atualizar_fornecedor_view(fornecedor_id: int, fornecedor_data: dict, session: Session = Depends(get_session)):
    fornecedor = atualizar_fornecedor(session, fornecedor_id, fornecedor_data)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

@router.delete("/fornecedor/{fornecedor_id}", response_model=Fornecedor)
async def apagar_fornecedor_view(fornecedor_id: int, session: Session = Depends(get_session)):
    fornecedor = apagar_fornecedor(session, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

# Rotas para Remédio
@router.get("/remedios/", response_model=list[Remedio])
async def listar_remedios_view(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return listar_remedios(session, skip, limit)

@router.post("/remedio/", response_model=Remedio)
async def criar_remedio_view(remedio_data: dict, session: Session = Depends(get_session)):
    return criar_remedio(session, remedio_data)

@router.get("/remedio/{remedio_id}", response_model=Remedio)
async def obter_remedio_view(remedio_id: int, session: Session = Depends(get_session)):
    remedio = obter_remedio_por_id(session, remedio_id)
    if not remedio:
        raise HTTPException(status_code=404, detail="Remédio não encontrado")
    return remedio

@router.get("/remedios/fornecedor/{fornecedor_id}", response_model=list[Remedio])
async def listar_remedios_por_fornecedor_view(fornecedor_id: int, session: Session = Depends(get_session)):
    return listar_remedios_por_fornecedor(session, fornecedor_id)

@router.get("/remedios/nome/{nome}", response_model=list[Remedio])
async def buscar_remedios_por_nome_view(nome: str, session: Session = Depends(get_session)):
    return buscar_remedios_por_nome(session, nome)

@router.get("/remedios/ano/{ano}", response_model=list[Remedio])
async def listar_remedios_por_ano_view(ano: int, session: Session = Depends(get_session)):
    return listar_remedios_por_ano(session, ano)

@router.get("/remedios/count", response_model=int)
async def contar_remedios_view(session: Session = Depends(get_session)):
    return contar_remedios(session)

@router.get("/remedios/ordenados/", response_model=list[Remedio])
async def listar_remedios_ordenados_view(ordenar_por: str = "preco", ordem: str = "asc", session: Session = Depends(get_session)):
    return listar_remedios_ordenados(session, ordenar_por, ordem)

@router.get("/remedios/com-fornecedor/", response_model=list[Remedio])
async def listar_remedios_com_fornecedor_view(session: Session = Depends(get_session)):
    return listar_remedios_com_fornecedor(session)
