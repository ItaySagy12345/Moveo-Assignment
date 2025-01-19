from sqlalchemy.ext.declarative import DeclarativeMeta
from database.session import DatabaseSession


def slug_generator(name: str, model: DeclarativeMeta) -> str:
    """
    Returns a unique slug
    """

    with DatabaseSession() as db:
        record_exists = model.find(db=db, slug=name)
        
        if record_exists:
            num_records: int = model.count(db=db)
            slug = f"{name}-{num_records - 1}"
        else:
            slug = name

        return slug


