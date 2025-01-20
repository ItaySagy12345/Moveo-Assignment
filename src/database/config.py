from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/moveo_db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)