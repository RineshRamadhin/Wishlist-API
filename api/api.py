from fastapi import APIRouter

from .endpoints.user import router as user_router
from .endpoints.list import router as list_router
from .endpoints.item import router as item_router

router = APIRouter()

router.include_router(user_router, prefix='/users')
router.include_router(list_router, prefix='/lists')
router.include_router(item_router, prefix='/items')
