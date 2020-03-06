from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .base import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    list = relationship("List", back_populates="items")
    list_id = Column(String, ForeignKey("list.id"))
    name = Column(String, index=True)
    url = Column(String, index=True)
    price = Column(Float, index=True)
    reason = Column(String, index=True)
    desire = Column(Integer, index=True)
    bought = Column(Boolean(), default=True)
