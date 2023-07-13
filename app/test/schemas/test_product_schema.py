import pytest

from app.schemas.category import Category
from app.schemas.product import Product, ProductInput, ProductOutput


def test_product_schema():
    product = Product(name="Kimchi-Soup", slug="kimchi-soup", price=22.99, stock=22)

    assert product.model_dump() == {
        "name": "Kimchi-Soup",
        "slug": "kimchi-soup",
        "price": 22.99,
        "stock": 22,
    }


def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(name="Kimchi Soup", slug="kimchi soup", price=22.99, stock=22)

    with pytest.raises(ValueError):
        product = Product(
            name="Kimchi-Soup", slug="kimchi-soup!", price=22.99, stock=22
        )

    with pytest.raises(ValueError):
        product = Product(name="Kimchi Soup", slug="Kimchi-soup", price=22.99, stock=22)


def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(name="Kimchi-Soup", slug="kimchi-soup", price=0, stock=22)


def test_product_input_schema():
    product = Product(name="Kimchi-Soup", slug="kimchi-soup", price=22.99, stock=22)

    product_input = ProductInput(category_slug="food", product=product)

    assert product_input.model_dump() == {
        "category_slug": "food",
        "product": {
            "name": "Kimchi-Soup",
            "slug": "kimchi-soup",
            "price": 22.99,
            "stock": 22,
        },
    }


def test_product_output_schema():
    category = Category(name="Animal", slug="animal")

    product_output = ProductOutput(
        id=1, name="Dog", slug="dog", price=10, stock=10, category=category
    )

    assert product_output.model_dump() == {
        "id": 1,
        "name": "Dog",
        "slug": "dog",
        "price": 10,
        "stock": 10,
        "category": {"name": "Animal", "slug": "animal"},
    }
