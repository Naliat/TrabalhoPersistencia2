# app/routes/remedio.py
from fastapi import APIRouter
from app.schemas.remedio import RemedioCreate
from app.crud.remedio import criar_remedio, obter_remedio_por_id, listar_remedios, listar_remedios_por_fornecedor, buscar_remedios_por_nome, listar_remedios_por_ano, contar_remedios, listar_remedios_ordenados, listar_remedios_com_fornecedor

router = APIRouter()

@router.get("/remedios/")
def obter_remedios():
    return listar_remedios()

@router.get("/remedios/{remedio_id}")
def obter_remedio(remedio_id: int):
    return obter_remedio_por_id(remedio_id)

@router.get("/remedios/fornecedor/{fornecedor_id}")
def obter_remedios_por_fornecedor(fornecedor_id: int):
    return listar_remedios_por_fornecedor(fornecedor_id)

@router.get("/remedios/busca")
def buscar_remedios(nome: str):
    return buscar_remedios_por_nome(nome)

@router.get("/remedios/validade/{ano}")
def obter_remedios_por_ano(ano: int):
    return listar_remedios_por_ano(ano)

@router.get("/remedios/contagem")
def contar_total_remedios():
    return {"quantidade": contar_remedios()}

@router.get("/remedios/ordenar")
def ordenar_remedios(ordenar_por: str = "preco", ordem: str = "asc"):
    return listar_remedios_ordenados(ordenar_por, ordem)

@router.get("/remedios/com_fornecedor")
def obter_remedios_com_fornecedor(preco_max: float = 100.0):
    return listar_remedios_com_fornecedor(preco_max)

@router.post("/remedios/")
def criar_remedio_endpoint(remedio: RemedioCreate):
    criar_remedio(remedio)
    return {"msg": "Remédio criado com sucesso"}
