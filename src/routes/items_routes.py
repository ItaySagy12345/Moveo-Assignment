from fastapi import APIRouter, Depends
from models.items_model import Item
from fastapi import status
from generics.base_response import BaseResponse
from dependencies.item_dep import item_dep
from dependencies.db_dep import db_dep
from sqlalchemy.orm import Session
from schemas.items_schema import ItemCreateSchema, ItemUpdateSchema
from utils.slug_generator import slug_generator


items_router = APIRouter()

@items_router.get("/items", tags=["items", "list"], response_model=BaseResponse[list[Item]], status_code=status.HTTP_200_OK)
async def list_items(db: Session = Depends(db_dep)):
    """
    Returns a list of items back to the client
    """

    items: list[Item] = Item.list(db=db)
    return BaseResponse(data=items)


@items_router.post("/items", tags=["items", "create"], response_model=BaseResponse[Item], status_code=status.HTTP_201_CREATED)
async def create_item(data: ItemCreateSchema, db: Session = Depends(db_dep)):
    """
    Creates an item and returns it to the client
    """

    slug: str = slug_generator(name=data.name, model=Item)
    create_item = ItemCreateSchema(
        slug=slug,
        name=data.name,
        description=data.description
    )
    item: Item = Item.create(db=db, data=create_item)
    return BaseResponse(data=item)
    

@items_router.get("/items/{slug}", tags=["items", "find"], response_model=BaseResponse[Item], status_code=status.HTTP_200_OK)
async def get_item(item: Item = Depends(item_dep)):
    """
    Returns an item by its slug to the client
    """

    return BaseResponse(data=item)


@items_router.put("/items/{slug}", tags=["items", "update"], response_model=BaseResponse[Item], status_code=status.HTTP_200_OK)
async def update_item(data: ItemUpdateSchema, db: Session = Depends(db_dep), item: Item = Depends(item_dep)):
    """
    Updates an item and returns it to the client
    """
    
    item: Item = item.update(db=db, id=item.id, data=data)
    return BaseResponse(data=item)


@items_router.delete("/items/{slug}", tags=["items", "delete"], response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(db: Session = Depends(db_dep), item: Item = Depends(item_dep)):
    """
    Deletes an item from the database
    """

    item.delete(db=db, id=item.id)