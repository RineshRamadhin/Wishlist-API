from typing import List

from crud.list import _list as crud_list
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.utils.db import get_db
from schemas.list import List as ListSchema, ListCreate, ListUpdate

router = APIRouter()


@router.get("/", response_model=List[ListSchema], tags=['Lists'])
def read_lists(
        db: Session = Depends(get_db),
):
    lists = crud_list.get_multi(db)
    return lists


@router.post("/", response_model=ListSchema, tags=['Lists'])
def create_list(
        *,
        db: Session = Depends(get_db),
        list_in: ListCreate,
):
    _list = crud_list.create(db, obj_in=list_in)
    return _list


@router.get("/{list_id}", response_model=ListSchema, tags=['Lists'])
def read_list_by_id(
        list_id: int,
        db: Session = Depends(get_db),
):
    _list = crud_list.get(db, id=list_id)
    return _list


@router.put("/{list_id}", response_model=ListSchema, tags=['Lists'])
def update_list(
        *,
        db: Session = Depends(get_db),
        list_id: int,
        list_in: ListUpdate,
):
    _list = crud_list.get(db, id=list_id)
    _list = crud_list.update(db, db_obj=_list, obj_in=list_in)
    return _list

@router.delete("/{list_id}", response_model=str, tags=['Lists'])
def delete_list(
        *,
        db: Session = Depends(get_db),
        list_id: int
):
    _list = crud_list.get(db, id=list_id)
    crud_list.remove(db, id=_list.id)
    return 'OK'
