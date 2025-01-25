from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session


def slug_generator(db: Session, name: str, model: DeclarativeMeta) -> str:
    """
    Returns a unique slug
    Param: db [Session]: The database session
    Param: name [String]: The name of the model that needs a slug
    Param model [DeclarativeMeta]: The model that needs a slug
    Return: [String]: The generated slug
    """

    record_exists = model.find(db=db, slug=name)
    
    if record_exists:
        num_records: int = model.count(db=db, name=name)
        slug = f"{name}-{num_records - 1}"
    else:
        slug = name

    return slug


