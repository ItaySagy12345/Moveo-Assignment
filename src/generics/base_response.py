from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    """
    Universal API response class
    """

    data: T
    meta: dict = {}