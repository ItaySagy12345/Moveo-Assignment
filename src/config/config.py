import os
from dotenv import load_dotenv


load_dotenv()

CONFIG = {
    "db" : {
        "db_user": os.getenv('DB_USER'),
        "db_password": os.getenv('DB_PASSWORD'),
        "db_host": os.getenv('DB_HOST'),
        "db_port": os.getenv('DB_PORT'),
        "db_name": os.getenv('DB_NAME'),
    }
}