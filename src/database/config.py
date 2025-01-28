from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.config import CONFIG


engine = create_engine(f'postgresql+psycopg2://{CONFIG["db"]["db_user"]}:{CONFIG["db"]["db_password"]}@{CONFIG["db"]["db_host"]}:{CONFIG["db"]["db_port"]}/{CONFIG["db"]["db_name"]}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)