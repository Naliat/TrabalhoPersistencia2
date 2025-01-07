from pydantic import BaseModel  

class EstoqueBase(BaseModel):  
    quantidade: int  
    data_validade: str  
    data_entrada_estoque: str  
    unidade_medida: str  

class EstoqueCreate(EstoqueBase):  
    remedio_id: int  

class EstoqueRead(EstoqueBase):  
    id_do_remedio: int  

    class Config:  
        orm_mode = True