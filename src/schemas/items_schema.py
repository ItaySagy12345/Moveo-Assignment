from pydantic import BaseModel
from typing import Optional


class ItemCreateSchema(BaseModel):
    """
    Schema for creating a new item
    """

    slug: Optional[str]
    name: str
    description: str


class ItemUpdateSchema(BaseModel):
    """
    Schema for updating an existing item
    """

    slug: str
    name: str
    description: str


class ItemSchema(BaseModel):
    """
    Schema for an item
    """

    slug: str
    name: str
    description: str

    class Config:
        from_attributes=True