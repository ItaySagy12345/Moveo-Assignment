from database.config import db


class DatabaseSession:
    """
    Database session context manager
    """
    
    def __init__(self):
        self.db = None

    def __enter__(self):
        self.db = db()
        return self.db

    def __exit__(self, exc_type):
        if exc_type is None:
            try:
                self.db.commit()
            except Exception:
                self.db.rollback()
                raise
        else:
            self.db.rollback()
        
        self.db.close()