from pydantic import BaseModel  

class RemedioBase(BaseModel):  
    nome: str  
    tarja: str  
    preco: float  
    validade: str  

class RemedioCreate(RemedioBase):  
    pass  

class RemedioRead(RemedioBase):  
    id: int  

    class Config:  
        orm_mode = True