from sqlalchemy.orm import Session
from database.config import Base
from sqlalchemy.ext.declarative import DeclarativeMeta
from abc import ABC
from pydantic import BaseModel


class CrudBase(ABC):
    """
    Abstract class for database models
    """

    def count(cls, db: Session):
        """
        Count method for database models
        Param: db [Session]: The database session
        Return [Integer]: The number of records
        """

        SQL = f"SELECT COUNT(*) FROM {cls.__tablename__}"

    def list(cls: DeclarativeMeta, db: Session):
        """
        List method for database models
        Param: db [Session]: The database session
        Return [List[Any]]: A list of the records
        """

        SQL = f"SELECT * FROM {cls.__tablename__}"

    def find(cls: DeclarativeMeta, db: Session, slug: str):
        """
        Find method for database models
        Param: db [Session]: The database session
        Param: id [Integer]: The record's id
        Return [Any]: The found record
        """

        SQL = f"SELECT * FROM {cls.__tablename__} WHERE id = {id}"

    def create(cls: DeclarativeMeta, db: Session, data: BaseModel):
        """
        Create method for database models
        Param: db [Session]: The database session
        Param: data [Any]: The data to insert
        Return [Integer]: The inserted record's id
        """

        SQL = f"INSERT INTO {cls.__tablename__} (column1, column2, column3, ...) VALUES (value1, value2, value3, ...)"

    def update(cls: DeclarativeMeta, db: Session, id: int, data: BaseModel):
        """
        Update method for database models
        Param: db [Session]: The database session
        Param: id [Integer]: The record's id
        Return [Integer]: The record's id
        """

        SQL = f"UPDATE INTO {cls.__tablename__} (column1, column2, column3, ...) VALUES (value1, value2, value3, ...)"

    def delete(cls: DeclarativeMeta, db: Session, id: int):
        """
        Delete method for database models
        Param: db [Session]: The database session
        Param: id [Integer]: The record's id
        Return [Integer]: The record's id
        """

        SQL = f"DELETE FROM {cls.__tablename__} WHERE id = {id}"
