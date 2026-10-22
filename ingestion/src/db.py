import logging 

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from . import config

logger = logging.getLogger(__name__)

def get_engine() -> Engine:
    return create_engine(config.DATABASE_URL, pool_pre_ping=True)


def ensure_schema(engine: Engine, schema : str) -> None:
    with engine.begin() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
    logger.info("Schema '%s' is ready", schema)