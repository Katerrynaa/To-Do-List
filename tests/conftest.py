from pytest import fixture 
from fastapi.testclient import TestClient
from sqlalchemy import delete

from main import app 
from src.config import read_config
from src.models import SessionLocal, ToDoModel



@fixture(scope="class")
def tasks_data():
    return {
        "title": "dinner",
        "description": "order restaurant",
    }


@fixture(scope="class")
def new_tasks_data():
    return {
        "title": "flight",
        "description": "book summer tickets",
    }


@fixture(scope="session")
def test_client():
    return TestClient(app)


@fixture(scope="class", autouse=True)
def test_session():
    with SessionLocal() as session:
        try:
            yield session 
        finally:
            session.close()


@fixture(scope="class", autouse=True)
def clean_db(test_session):
    test_session.execute(delete(ToDoModel))