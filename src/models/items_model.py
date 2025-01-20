from sqlalchemy import Column, Integer, String
from src.database.crud_base import CrudBase
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Item(CrudBase, Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)