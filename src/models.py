from sqlalchemy import String, Integer, Boolean, Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from src.config import read_config

config = read_config()
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


class ToDoModel:
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(300))
    is_completed = Boolean()