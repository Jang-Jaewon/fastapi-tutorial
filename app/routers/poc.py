from fastapi import APIRouter, Depends
from fastapi_pagination import LimitOffsetPage, Page, add_pagination, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_paginate
from sqlalchemy.orm import Session

from app.db.models import Category as CategoryModel
from app.routers.deps import get_db_session
from app.schemas.category import CategoryOutput

router = APIRouter(prefix="/poc", tags=["POC"])


@router.get("/list", response_model=Page[CategoryOutput])
@router.get("/list/limit-offset", response_model=LimitOffsetPage[CategoryOutput])
def list_categories():
    categories = [
        CategoryOutput(name=f"category {n}", slug=f"category-{n}", id=n)
        for n in range(100)
    ]

    return paginate(categories)


@router.get("/list/sqlalchemy", response_model=Page[CategoryOutput])
@router.get(
    "/list/limit-offset/sqlalchemy", response_model=LimitOffsetPage[CategoryOutput]
)
def list_categories_sqlalchemy(db_session: Session = Depends(get_db_session)):
    categories = db_session.query(CategoryModel)
    return sqlalchemy_paginate(categories)


add_pagination(router)
