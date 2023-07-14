from fastapi import APIRouter, Depends
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.orm import Session

from app.db.models import Category as CategoryModel
from app.routers.deps import get_db_session
from app.schemas.category import CategoryOutput

router = APIRouter(prefix="/poc", tags=["POC"])


@router.get("/list", response_model=Page[CategoryOutput])
def list_categories():
    categories = [
        CategoryOutput(name=f"category {n}", slug=f"category-{n}", id=n)
        for n in range(100)
    ]

    return paginate(categories)


add_pagination(router)
