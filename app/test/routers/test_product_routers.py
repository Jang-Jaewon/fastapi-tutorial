from fastapi import status
from fastapi.testclient import TestClient

from app.db.models import Product as ProductModel
from app.main import app

client = TestClient(app)


def test_add_product_route(db_session, categories_on_db):
    body = {
        "category_slug": categories_on_db[0].slug,
        "product": {
            "name": "Kimchi-Soup",
            "slug": "kimchi-soup",
            "price": 22.99,
            "stock": 22,
        },
    }

    response = client.post("/product/add", json=body)
    assert response.status_code == status.HTTP_201_CREATED

    products_on_db = db_session.query(ProductModel).all()
    assert len(products_on_db) == 1

    db_session.delete(products_on_db[0])
    db_session.commit()


def test_add_product_route_invalid_category_slug(db_session):
    body = {
        "category_slug": "invalid",
        "product": {
            "name": "Kimchi-Soup",
            "slug": "kimchi-soup",
            "price": 22.99,
            "stock": 22,
        },
    }

    response = client.post("/product/add", json=body)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    products_on_db = db_session.query(ProductModel).all()
    assert len(products_on_db) == 0


def test_update_product_route(db_session, product_on_db):
    body = {"name": "Updated-Car", "slug": "updated-car", "price": 23.88, "stock": 10}

    response = client.put(f"/product/update/{product_on_db.id}", json=body)

    assert response.status_code == status.HTTP_200_OK

    db_session.refresh(product_on_db)

    product_on_db.name == "Updated-Car"
    product_on_db.slug == "updated-car"
    product_on_db.price == 23.88
    product_on_db.stock == 10


def test_update_product_route_invalid_id():
    body = {"name": "Updated-Car", "slug": "updated-car", "price": 23.88, "stock": 10}

    response = client.put(f"/product/update/1", json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_product_route(db_session, product_on_db):
    response = client.delete(f"/product/delete/{product_on_db.id}")

    assert response.status_code == status.HTTP_200_OK

    products_on_db = db_session.query(ProductModel).all()

    assert len(products_on_db) == 0


def test_delete_product_route_invalid_id():
    response = client.delete(f"/product/delete/1")

    assert response.status_code == status.HTTP_404_NOT_FOUND
