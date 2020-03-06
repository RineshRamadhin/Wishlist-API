from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    price: Optional[float] = None
    reason: Optional[str] = None
    desire: Optional[int] = None
    bought: Optional[bool] = None


class ItemBaseInDB(ItemBase):
    id: int = None

    class Config:
        orm_mode = True


class ItemCreate(ItemBaseInDB):
    name: str
    url: str
    price: float
    reason: str
    desire: int
    bought: bool


class ItemUpdate(ItemBaseInDB):
    name: Optional[str] = None
    url: Optional[str] = None
    price: Optional[float] = None
    reason: Optional[str] = None
    desire: Optional[str] = 0
    bought: Optional[bool] = False


class Item(ItemBaseInDB):
    pass


class ItemInDB(ItemBaseInDB):
    pass
