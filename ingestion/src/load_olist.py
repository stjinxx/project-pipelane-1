import logging 
from pathlib import Path 

import pandas as pd

from . import config
from .db import ensure_schema, get_engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger("load_olist")


def table_name_for(csv_path: Path) -> str:
    stem = csv_path.stem
    if stem.endswith("_dataset"):
        stem = stem[: -len("_dataset")]
    return stem.lower()

def load_file(engine, csv_path: Path) -> None:
    table = table_name_for(csv_path)
    logger.info("Loading %s -> %s.%s", csv_path.name, config.RAW_SCHEMA, table) 

    df = pd.read_csv(csv_path,encoding="utf-8")
    logger.info("Read %d rows, %d colums", len(df), len(df.columns))

    df.to_sql(
        name=table,
        con=engine,
        schema=config.RAW_SCHEMA,
        if_exists="replace",
        index=False,
        method="multi",
        chunksize=5000,
    )
    logger.info("Loaded %s.%s (%d rows)", config.RAW_SCHEMA, table, len(df))

def main() -> None:
    data_dir = Path(config.DATA_DIR)
    if not data_dir.exists():
        raise FileNotFoundError(f"Data dir not found: {data_dir}")

    csv_files = sorted(data_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV file {data_dir}")

    logger.info("Found %d CSV files", len(csv_files))

    engine = get_engine()
    ensure_schema(engine, config.RAW_SCHEMA)

    for csv_path in csv_files: 
        load_file(engine, csv_path)

    logger.info("All file loaded succesfully")

if __name__ == "__main__":
    main()