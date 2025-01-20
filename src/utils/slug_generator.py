from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session


def slug_generator(db: Session, name: str, model: DeclarativeMeta) -> str:
    """
    Returns a unique slug
    """

    record_exists = model.find(db=db, slug=name)
    
    if record_exists:
        num_records: int = model.count(db=db, name=name)
        slug = f"{name}-{num_records - 1}"
    else:
        slug = name

    return slug


