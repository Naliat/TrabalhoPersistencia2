from app.models.remedio import Remedio
from sqlmodel import Session, create_engine
from app.models import Remedio  # Importar as classes do banco de dados

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Exemplo com SQLite, ajuste conforme seu caso

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

def get_db():
    with Session(engine) as session:
        yield session
