from models.item import Item
from schemas.item import ItemCreate, ItemUpdate
from .base import CRUDBase


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    pass


item = CRUDItem(Item)
