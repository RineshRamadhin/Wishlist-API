import uuid

from typing import Optional
from pydantic import BaseModel


class ListBase(BaseModel):
    user_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    sharable: Optional[bool] = None
    color: Optional[str] = None


class ListBaseInDB(ListBase):
    id: uuid.UUID = uuid.uuid4()

    class Config:
        orm_mode = True


class ListCreate(ListBaseInDB):
    user_id: int
    title: str
    description: str
    sharable: bool
    color: str


class ListUpdate(ListBaseInDB):
    title: Optional[str] = None
    description: Optional[str] = None
    sharable: Optional[bool] = True
    color: Optional[str] = True


class List(ListBaseInDB):
    pass


class ListInDB(ListBaseInDB):
    pass
