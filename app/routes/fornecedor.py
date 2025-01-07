# app/routes/fornecedor.py
from fastapi import APIRouter
from app.schemas.fornecedor import FornecedorCreate
from app.crud.fornecedor import criar_fornecedor, obter_fornecedor_por_id, listar_fornecedores, contar_fornecedores

router = APIRouter()

@router.get("/fornecedores/{fornecedor_id}")
def obter_fornecedor(fornecedor_id: int):
    return obter_fornecedor_por_id(fornecedor_id)

@router.get("/fornecedores/")
def obter_fornecedores():
    return listar_fornecedores()

@router.get("/fornecedores/contagem")
def contar_total_fornecedores():
    return {"quantidade": contar_fornecedores()}

@router.post("/fornecedores/")
def criar_fornecedor_endpoint(fornecedor: FornecedorCreate):
    criar_fornecedor(fornecedor)
    return {"msg": "Fornecedor criado com sucesso"}
