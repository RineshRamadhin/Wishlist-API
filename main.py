from fastapi import FastAPI
from api.api import router as api_router
from starlette.requests import Request
from db.session import Session, engine
from models.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Wishlist API')

app.include_router(api_router, prefix='/api')

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response
