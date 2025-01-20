from typing import Generator
from database.config import SessionLocal
from sqlalchemy.orm import Session


def db_dep() -> Generator:
    """
    Yields the db session
    """
        
    db: Session = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()