import pytest
from app.schemas.category import Category


def test_category_schema():
    category = Category(
        name="Food",
        slug="food"
    )

    assert category.model_dump() == {
        "name": "Food",
        "slug": "food"
    }


def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name="Food",
            slug="bed food"
        )

    with pytest.raises(ValueError):
        category = Category(
            name="Food",
            slug="food@"
        )

    with pytest.raises(ValueError):
        category = Category(
            name="Food",
            slug="Food"
        )
