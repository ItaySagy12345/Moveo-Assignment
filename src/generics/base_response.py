from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    Universal API response class
    """

    data: dict = {}
    meta: dict = {}