import pytest

from app.schemas.user import User


def test_user_schema():
    user = User(username="jaewon", password="pass#")
    assert user.model_dump() == {"username": "jaewon", "password": "pass#"}


def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username="jaewon!@", password="pass#")
