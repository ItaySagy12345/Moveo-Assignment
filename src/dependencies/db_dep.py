from typing import Generator
from database.session import DatabaseSession


def db_dep() -> Generator:
    """
    Yields the db session
    """
        
    with DatabaseSession() as db:
        yield db