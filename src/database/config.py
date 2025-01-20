from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/moveo')
db: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)