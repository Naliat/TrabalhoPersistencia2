import logging
from sqlmodel import create_engine, Session
from typing import Generator
from dotenv import load_dotenv
import os

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtenha a URL do banco de dados do arquivo .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Verifique se a variável DATABASE_URL está definida corretamente
if not SQLALCHEMY_DATABASE_URL:
    logger.error("A variável DATABASE_URL não foi definida no arquivo .env!")
    raise ValueError("A variável DATABASE_URL não foi definida no arquivo .env!")

# Criação do engine de conexão com o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Log de conexão com o banco de dados
logger.info(f"Conectando ao banco de dados em {SQLALCHEMY_DATABASE_URL}")

# Função para obter a sessão do banco de dados
def get_session() -> Generator[Session, None, None]:
    """Retorna uma sessão de banco de dados"""
    with Session(engine) as session:
        yield session
