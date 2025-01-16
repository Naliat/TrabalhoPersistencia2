import sqlite3
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy import event, Engine
from dotenv import load_dotenv
import logging
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurar o logger
logging.basicConfig(level=logging.INFO)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Configuração do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Verificar se a variável DATABASE_URL está configurada corretamente
if not DATABASE_URL:
    raise ValueError("A variável DATABASE_URL não foi definida no arquivo .env!")

# Criar o engine de conexão
engine = create_engine(DATABASE_URL)

# Criar a(s) tabela(s) no banco de dados
def create_db_and_tables() -> None:
    """Cria as tabelas no banco de dados com base nos modelos definidos"""
    SQLModel.metadata.create_all(engine)

# Função para obter uma sessão do banco de dados
def get_session() -> Session:
    """Retorna uma sessão do banco de dados"""
    return Session(engine)

# Configuração específica para SQLite (habilitar suporte a chaves estrangeiras)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:  # Somente para SQLite
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")  # Ativa suporte a chaves estrangeiras
        cursor.close()
