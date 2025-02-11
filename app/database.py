from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATEBASE_URL = 'sqlite:///app.db'

engine = create_engine(
    DATEBASE_URL, 
    connect_args={"check_same_thread": False}
)
    
session = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()