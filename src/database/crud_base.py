from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy.ext.declarative import DeclarativeMeta
from src.errors.errors import NotFoundError
from typing import Union
from src.utils.logger import logger


class CrudBase:
    """
    Abstract class for database models
    """

    @classmethod
    def count(cls, db: Session, **kwargs) -> int:
        """
        Count method for database models
        Param: db [Session]: The database session
        Return [Integer]: The number of records
        """

        query = db.query(cls)

        for key, value in kwargs.items():
            query = query.filter(getattr(cls, key) == value)

        return query.count()

    @classmethod
    def list(cls: DeclarativeMeta, db: Session) -> Union[list[DeclarativeMeta], None]:
        """
        List method for database models
        Param: db [Session]: The database session
        Return [Union[list[DeclarativeMeta], None]]: A list of the records
        """

        models = db.query(cls).all()

        if not models:
            return []
        
        return models

    @classmethod
    def find(cls: DeclarativeMeta, db: Session, slug: str) -> Union[DeclarativeMeta, None]:
        """
        Find method for database models
        Param: db [Session]: The database session
        Param: id [Integer]: The record's id
        Return [Union[DeclarativeMeta, None]]: The found record if there was one
        """

        return db.query(cls).filter(cls.slug == slug).first() 

    @classmethod
    def create(cls: DeclarativeMeta, db: Session, data: BaseModel) -> DeclarativeMeta:
        """
        Create method for database models
        Param: db [Session]: The database session
        Param: data [Any]: The data to insert
        Return [DeclarativeMeta]: The created record
        """

        model_data = cls(**data.model_dump())
        db.add(model_data)
        db.commit()
        db.refresh(model_data)
        return model_data


    @classmethod
    def update(cls: DeclarativeMeta, db: Session, id: int, data: BaseModel) -> DeclarativeMeta:
        """
        Update method for database models
        Param: db [Session]: The database session
        Param: id [Integer]: The record's id
        Return [DeclarativeMeta]: The updated record
        """

        try:
            model = db.query(cls).filter(cls.id == id).first()

            if not model:
                raise NotFoundError('Resource not found')
            
            update_data = data.model_dump()

            for key, value in update_data.items():
                if hasattr(model, key):
                    setattr(model, key, value)

            db.commit()
            db.refresh(model)
            return model

        except Exception as e:
            logger.info(e)
            db.rollback()
            return

    @classmethod
    def delete(cls: DeclarativeMeta, db: Session, id: int):
        """
        Delete method for database models
        Param: db [Session]: The database session
        Param: id [Integer]: The record's id
        Return [Integer]: The record's id
        """

        item = db.query(cls).filter(cls.id == id).first()

        if not item:
            raise NotFoundError('Resource not found')

        db.delete(item)
        db.commit()
