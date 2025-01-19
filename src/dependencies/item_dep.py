from models.items_model import Item
from database.session import DatabaseSession


def item_dep(slug: str) -> Item:
    """
    Returns the item by its slug
    """

    with DatabaseSession() as db:
        item: Item = Item.find(db=db, slug=slug)
        return item