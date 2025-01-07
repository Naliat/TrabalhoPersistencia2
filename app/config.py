# app/config.py
from sqlmodel import SQLModel, create_engine

# Definindo a URL do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Criando o engine do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Função para criar o banco de dados e as tabelas
def init_db():
    SQLModel.metadata.create_all(bind=engine)
