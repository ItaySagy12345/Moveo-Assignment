from sqlalchemy import Column, Integer, String
from database.config import Base
from database.crud_base import CrudBase

class Item(Base, CrudBase):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)