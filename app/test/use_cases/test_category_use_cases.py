import pytest
from fastapi.exceptions import HTTPException
from fastapi_pagination import Page

from app.db.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput
from app.use_cases.category import CategoryUseCases


def test_add_category_uc(db_session):
    uc = CategoryUseCases(db_session)

    category = Category(name="Food", slug="food")

    uc.add_category(category=category)

    categories_on_db = db_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    assert categories_on_db[0].name == "Food"
    assert categories_on_db[0].slug == "food"

    db_session.delete(categories_on_db[0])
    db_session.commit()


def test_list_categories_uc(db_session, categories_on_db):
    uc = CategoryUseCases(db_session=db_session)

    page = uc.list_categories(page=1, size=2)

    assert type(page) == Page
    assert len(page.items) == 2
    assert page.total == 4
    assert page.page == 1
    assert page.size == 2
    assert page.pages == 2


def test_delete_category(db_session):
    category_model = CategoryModel(name="Food", slug="food")
    db_session.add(category_model)
    db_session.commit()

    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id=category_model.id)

    category_model = db_session.query(CategoryModel).first()
    assert category_model is None


def test_delete_category_non_exist(db_session):
    uc = CategoryUseCases(db_session=db_session)
    with pytest.raises(HTTPException):
        uc.delete_category(id=1)
