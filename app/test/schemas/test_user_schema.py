from datetime import datetime

import pytest

from app.schemas.user import TokenData, User


def test_user_schema():
    user = User(username="jaewon", password="pass#")
    assert user.model_dump() == {"username": "jaewon", "password": "pass#"}


def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username="jaewon!@", password="pass#")


def test_token_date():
    expires_at = datetime.now()
    token_data = TokenData(access_token="test token", expires_at=expires_at)

    assert token_data.model_dump() == {
        "access_token": "test token",
        "expires_at": expires_at,
    }
