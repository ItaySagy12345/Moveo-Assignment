from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseResponse(Generic[T], BaseModel):
    """
    Universal API response class
    """

    data: dict = {}
    meta: dict = {}