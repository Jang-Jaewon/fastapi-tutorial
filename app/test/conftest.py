import pytest

from app.db.connection import Session
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModel(name="Food", slug="food"),
        CategoryModel(name="Animal", slug="animal"),
        CategoryModel(name="Life", slug="life"),
        CategoryModel(name="Car", slug="car"),
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModel(name="Car", slug="car")
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name="Volvo-XC",
        slug="volvo-xc",
        price=100.99,
        stock=20,
        category_id=category.id,
    )

    db_session.add(product)
    db_session.commit()

    yield product

    db_session.delete(product)
    db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def products_on_db(db_session):
    category = CategoryModel(name="Animal", slug="animal")
    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)

    products = [
        ProductModel(
            name="Dog", slug="dog", price=100, stock=10, category_id=category.id
        ),
        ProductModel(
            name="Cat", slug="cat", price=100, stock=10, category_id=category.id
        ),
        ProductModel(
            name="Hot-Dog", slug="hot-dog", price=100, stock=10, category_id=category.id
        ),
        ProductModel(
            name="Dog-Bear", slug="bear", price=100, stock=10, category_id=category.id
        ),
    ]

    for product in products:
        db_session.add(product)
    db_session.commit()

    for product in products:
        db_session.refresh(product)

    yield products

    for product in products:
        db_session.delete(product)

    db_session.delete(category)
    db_session.commit()
