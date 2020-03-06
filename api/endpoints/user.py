from typing import List

from crud.user import user as crud_user

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.db import get_db
from schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.get("/", response_model=List[User], tags=['Users'])
def read_users(
        db: Session = Depends(get_db),
):
    users = crud_user.get_multi(db)
    return users


@router.post("/", response_model=User, tags=['Users'])
def create_user(
        *,
        db: Session = Depends(get_db),
        user_in: UserCreate,
):
    user = crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud_user.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=User, tags=['Users'])
def read_user_by_id(
        user_id: int,
        db: Session = Depends(get_db),
):
    user = crud_user.get(db, id=user_id)
    return user


@router.put("/{user_id}", response_model=User, tags=['Users'])
def update_user(
        *,
        db: Session = Depends(get_db),
        user_id: int,
        user_in: UserUpdate,
):
    user = crud_user.get(db, id=user_id)
    user = crud_user.update(db, db_obj=user, obj_in=user_in)
    return user

@router.delete("/{user_id}", response_model=str, tags=['Users'])
def delete_user(
        *,
        db: Session = Depends(get_db),
        user_id: int
):
    user = crud_user.get(db, id=user_id)
    crud_user.remove(db, id=user.id)
    return 'OK'
