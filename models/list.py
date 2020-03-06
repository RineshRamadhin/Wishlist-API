import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class List(Base):
    id = Column(String, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="lists")
    title = Column(String, index=True)
    description = Column(String, index=True)
    sharable = Column(Boolean(), default=True)
    color = Column(String)
    items = relationship("Item", back_populates="list")
