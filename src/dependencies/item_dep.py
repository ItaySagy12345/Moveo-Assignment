from fastapi import Depends
from dependencies.db_dep import db_dep
from models.items_model import Item
from sqlalchemy.orm import Session
from errors.errors import ArgumentsError


def item_dep(slug: str, db: Session = Depends(db_dep)) -> Item:
    """
    Returns the item by its slug
    """
    
    item: Item = Item.find(db=db, slug=slug)
    
    if not item:
        raise ArgumentsError('Unprocessable, error with one or more arguments provided')

    return item