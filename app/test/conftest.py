import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()
