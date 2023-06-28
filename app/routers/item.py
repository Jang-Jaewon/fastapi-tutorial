from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.oauth2 import require_user

from .. import models, schemas
from ..database import get_db

router = APIRouter()


@router.get("/", response_model=schemas.ListItemResponse)
def get_items(
    db: Session = Depends(get_db),
    limit: int = 10,
    page: int = 1,
    search: str = "",
    user_id: int = Depends(require_user),
):
    skip = (page - 1) * limit

    items = (
        db.query(models.Item)
        .group_by(models.Item.id)
        .filter(models.Item.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    return {"status": "success", "results": len(items), "items": items}


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.ItemResponse
)
def create_item(
    item: schemas.CreateItemSchema,
    db: Session = Depends(get_db),
    owner_id: int = Depends(require_user),
):
    item.user_id = owner_id
    new_item = models.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.put("/{id}", response_model=schemas.ItemResponse)
def update_item(
    id: int,
    item: schemas.UpdateItemSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(require_user),
):
    item_query = db.query(models.Item).filter(models.Item.id == id)
    updated_item = item_query.first()

    if not updated_item:
        raise HTTPException(
            status_code=status.HTTP_200_OK, detail=f"No item with this id: {id} found"
        )
    if updated_item.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to perform this action",
        )
    item.user_id = user_id
    item_query.update(item.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return updated_item


@router.get("/{id}", response_model=schemas.ItemResponse)
def get_item(
    id: int, db: Session = Depends(get_db), user_id: int = Depends(require_user)
):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    print("user", item.owner)

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No item with this id: {id} found",
        )

    return item


@router.delete("/{id}")
def delete_item(
    id: str, db: Session = Depends(get_db), user_id: int = Depends(require_user)
):
    item_query = db.query(models.Item).filter(models.Item.id == id)
    item = item_query.first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No item with this id: {id} found",
        )

    if item.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to perform this action",
        )
    item_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)