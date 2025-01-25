from fastapi import APIRouter, Depends, Request
from src.models.items_model import Item
from fastapi import status
from src.generics.base_response import BaseResponse
from src.dependencies.item_dep import item_dep
from src.dependencies.db_dep import db_dep
from sqlalchemy.orm import Session
from src.schemas.items_schema import ItemCreateSchema, ItemUpdateSchema, ItemSchema
from src.utils.slug_generator import slug_generator
from src.kafka.producer import kafka_producer 
from src.kafka.utils.topics import KafkaTopics


items_router = APIRouter()

@items_router.get("/items", tags=["items", "list"], response_model=BaseResponse[list[ItemSchema]], status_code=status.HTTP_200_OK)
async def list_items(db: Session = Depends(db_dep)):
    """
    Returns a list of items back to the client
    """

    items: list[Item] = Item.list(db=db)
    items_data: list[ItemSchema] = [ItemSchema.model_validate(item) for item in items]
    return BaseResponse(data=items_data)


@items_router.post("/items", tags=["items", "create"], response_model=BaseResponse[ItemSchema], status_code=status.HTTP_201_CREATED)
async def create_item(request: Request, data: ItemCreateSchema, db: Session = Depends(db_dep)):
    """
    Creates an item and returns it to the client
    """

    slug: str = slug_generator(db=db, name=data.name, model=Item)
    create_item = ItemCreateSchema(
        slug=slug,
        name=data.name,
        description=data.description
    )
    item: Item = Item.create(db=db, data=create_item)
    item_data: ItemSchema = ItemSchema.model_validate(item)

    event_message = f"Method: {request.method} | URL: {str(request.url)} | Item ID: {item.id} | Slug: {item_data.slug} | Name: {item_data.name} | Description: {item_data.description}"
    kafka_producer.produce(topic=KafkaTopics.ITEM_CREATED, message=event_message)

    return BaseResponse(data=item_data)
    

@items_router.get("/items/{slug}", tags=["items", "find"], response_model=BaseResponse[ItemSchema], status_code=status.HTTP_200_OK)
async def get_item(item: Item = Depends(item_dep)):
    """
    Returns an item by its slug to the client
    """

    item_data: ItemSchema = ItemSchema.model_validate(item)
    return BaseResponse(data=item_data)


@items_router.put("/items/{slug}", tags=["items", "update"], response_model=BaseResponse[ItemSchema], status_code=status.HTTP_200_OK)
async def update_item(request: Request, data: ItemUpdateSchema, db: Session = Depends(db_dep), item: Item = Depends(item_dep)):
    """
    Updates an item and returns it to the client
    """
    
    item: Item = item.update(db=db, id=item.id, data=data)

    event_message = f"Method: {request.method} | URL: {str(request.url)} | Item ID: {item.id} | Slug: {item.slug} | Name: {item.name} | Description: {item.description}"
    kafka_producer.produce(topic=KafkaTopics.ITEM_UPDATED, message=event_message)

    return BaseResponse(data=item)


@items_router.delete("/items/{slug}", tags=["items", "delete"], response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(db: Session = Depends(db_dep), item: Item = Depends(item_dep)):
    """
    Deletes an item from the database
    """

    item.delete(db=db, id=item.id)