from sqlalchemy import String, Integer, DateTime, Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from src.config import read_config


config = read_config()
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


class ToDoModel(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(300))
    is_completed = Column(DateTime, default=None)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(255))