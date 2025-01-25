from fastapi import HTTPException, status
from typing import Optional


class NotFoundError(HTTPException):
    """
    A Not Found error class, returns status code 404
    """
        
    def __init__(self, message: Optional[str]):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)

class ArgumentsError(HTTPException):
    """
    An Arguments error class, returns status code 422
    """
     
    def __init__(self, message: Optional[str]):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=message)