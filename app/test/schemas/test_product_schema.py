import pytest
from app.schemas.product import Product


def test_product_schema():
    product = Product(
        name="Kimchi-Soup",
        slug="kimchi-soup",
        price=22.99,
        stock=22
    )

    assert product.dict() == {
        "name": "Kimchi-Soup",
        "slug": "kimchi-soup",
        "price": 22.99,
        "stock": 22
    }


def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name="Kimchi Soup",
            slug="kimchi soup",
            price=22.99,
            stock=22
        )

    with pytest.raises(ValueError):
        product = Product(
            name="Kimchi-Soup",
            slug="kimchi-soup!",
            price=22.99,
            stock=22
        )

    with pytest.raises(ValueError):
        product = Product(
            name="Kimchi Soup",
            slug="Kimchi-soup",
            price=22.99,
            stock=22
        )


def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name="Kimchi-Soup",
            slug="kimchi-soup",
            price=0,
            stock=22
        )
