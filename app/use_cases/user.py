from decouple import config
from fastapi import status
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models import User as UserModel
from app.schemas.user import User

crypt_context = CryptContext(schemes=["sha256_crypt"])

# SECRET_KEY = config("SECRET_KEY")
# ALGORITHM = config("ALGORITHM")


class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def register_user(self, user: User):
        user_on_db = UserModel(
            username=user.username, password=crypt_context.hash(user.password)
        )

        self.db_session.add(user_on_db)

        try:
            self.db_session.commit()
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )
