from models.list import List
from schemas.list import ListCreate, ListUpdate
from .base import CRUDBase


class CRUDList(CRUDBase[List, ListCreate, ListUpdate]):
    pass


_list = CRUDList(List)
