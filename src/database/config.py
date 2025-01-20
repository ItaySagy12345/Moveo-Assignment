from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# For use when running on local machine outside of docker
# engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/moveo_db')

engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres:5432/moveo_db')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)