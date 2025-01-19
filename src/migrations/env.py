from __future__ import with_statement
from logging.config import fileConfig
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from sqlalchemy import create_engine
from alembic import context

from src.models.items_model import Item
from src.database.config import Base

# This is the Alembic Config object
config = context.config

# Set up logging
fileConfig(config.config_file_name)

# Set the target metadata to your Base.metadata
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    engine = create_engine(config.get_main_option("sqlalchemy.url"))
    connection = engine.connect()
    context.configure(
        connection=connection, target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()

# Run migrations depending on the mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
