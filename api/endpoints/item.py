from typing import List

from crud.item import item as crud_item
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.utils.db import get_db
from schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter()


@router.get("/", response_model=List[Item], tags=['Items'])
def read_items(
        db: Session = Depends(get_db),
):
    items = crud_item.get_multi(db)
    return items


@router.post("/", response_model=Item, tags=['Items'])
def create_item(
        *,
        db: Session = Depends(get_db),
        item_in: ItemCreate,
):
    item = crud_item.create(db, obj_in=item_in)
    return item


@router.get("/{item_id}", response_model=Item, tags=['Items'])
def read_item_by_id(
        item_id: int,
        db: Session = Depends(get_db),
):
    item = crud_item.get(db, id=item_id)
    return item


@router.put("/{item_id}", response_model=Item, tags=['Items'])
def update_item(
        *,
        db: Session = Depends(get_db),
        item_id: int,
        item_in: ItemUpdate,
):
    item = crud_item.get(db, id=item_id)
    item = crud_item.update(db, db_obj=item, obj_in=item_in)
    return item

@router.delete("/{item_id}", response_model=str, tags=['Items'])
def delete_item(
        *,
        db: Session = Depends(get_db),
        item_id: int
):
    item = crud_item.get(db, id=item_id)
    crud_item.remove(db, id=item.id)
    return 'OK'
