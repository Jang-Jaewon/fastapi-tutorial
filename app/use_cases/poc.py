from fastapi_pagination import Params, paginate

from app.schemas.category import CategoryOutput


def list_categories_uc(page: int = 1, size: int = 50):
    categories = [
        CategoryOutput(name=f"category {n}", slug=f"category-{n}", id=n)
        for n in range(100)
    ]

    params = Params(page=page, size=size)
    return paginate(categories, params=params)
