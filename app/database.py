import sqlite3
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy import event, Engine
from dotenv import load_dotenv
import logging
import os


load_dotenv()

logging.basicConfig(level=logging.INFO)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError("A variável DATABASE_URL não foi definida no arquivo .env!")


engine = create_engine(DATABASE_URL)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Retorna uma sessão do banco de dados"""
    return Session(engine)


 
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:   
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
