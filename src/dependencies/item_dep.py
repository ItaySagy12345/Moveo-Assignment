from fastapi import Depends
from src.dependencies.db_dep import db_dep
from src.models.items_model import Item
from sqlalchemy.orm import Session
from src.errors.errors import ArgumentsError


def item_dep(slug: str, db: Session = Depends(db_dep)) -> Item:
    """
    Returns the item by its slug
    Param: slug [String]: The slug of the item to return
    Param: db [Session]: The database session
    Return: [Item]: The item model
    Raises: ArgumentsError
    """
    
    item: Item = Item.find(db=db, slug=slug)
    
    if not item:
        raise ArgumentsError('Unprocessable, error with one or more arguments provided')

    return item