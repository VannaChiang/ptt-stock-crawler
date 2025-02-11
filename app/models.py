from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base

class article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    link = Column(String, unique=True)
    author = Column(String)
    date = Column(String)
    push_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)