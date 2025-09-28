import logging
import duckdb
from datetime import datetime

DB_PATH = "nyc_tlc.duckdb"
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"

SERVICES = ["yellow", "green"]
START_YEAR = 2015
END_YEAR = datetime.now().year
MONTHS = list(range(1, 13))

logging.basicConfig(
    filename="etl.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)

con = duckdb.connect(DB_PATH)

con.execute("""
CREATE TABLE IF NOT EXISTS yellow_taxi_trip_data (
    vendorid                INTEGER,
    tpep_pickup_datetime    TIMESTAMP,
    tpep_dropoff_datetime   TIMESTAMP,
    passenger_count         INTEGER,
    trip_distance           DOUBLE,
    ratecodeid              INTEGER,
    pulocationid            INTEGER,
    dolocationid            INTEGER,
    payment_type            INTEGER,
    fare_amount             DOUBLE,
    extra                   DOUBLE,
    mta_tax                 DOUBLE,
    tip_amount              DOUBLE,
    tolls_amount            DOUBLE,
    improvement_surcharge   DOUBLE,
    total_amount            DOUBLE,
    congestion_surcharge    DOUBLE,
    year                    INTEGER
);
""")

con.execute("""
CREATE TABLE IF NOT EXISTS green_taxi_trip_data (
    vendorid                INTEGER,
    lpep_pickup_datetime    TIMESTAMP,
    lpep_dropoff_datetime   TIMESTAMP,
    passenger_count         INTEGER,
    trip_distance           DOUBLE,
    ratecodeid              INTEGER,
    pulocationid            INTEGER,
    dolocationid            INTEGER,
    payment_type            INTEGER,
    fare_amount             DOUBLE,
    extra                   DOUBLE,
    mta_tax                 DOUBLE,
    tip_amount              DOUBLE,
    tolls_amount            DOUBLE,
    improvement_surcharge   DOUBLE,
    total_amount            DOUBLE,
    congestion_surcharge    DOUBLE,
    year                    INTEGER
);
""")

def insert_parquet(url: str, service: str):
    """Insert Parquet file directly into DuckDB table with explicit column mapping"""
    try:
        if service == "yellow":
            con.execute(f"""
                INSERT INTO yellow_taxi_trip_data
                SELECT 
                    vendorid,
                    tpep_pickup_datetime,
                    tpep_dropoff_datetime,
                    passenger_count,
                    trip_distance,
                    ratecodeid,
                    pulocationid,
                    dolocationid,
                    payment_type,
                    fare_amount,
                    extra,
                    mta_tax,
                    tip_amount,
                    tolls_amount,
                    improvement_surcharge,
                    total_amount,
                    congestion_surcharge,
                    EXTRACT(YEAR FROM tpep_pickup_datetime) AS year
                FROM read_parquet('{url}')
            """)
        else:  # green
            con.execute(f"""
                INSERT INTO green_taxi_trip_data
                SELECT 
                    vendorid,
                    lpep_pickup_datetime,
                    lpep_dropoff_datetime,
                    passenger_count,
                    trip_distance,
                    ratecodeid,
                    pulocationid,
                    dolocationid,
                    payment_type,
                    fare_amount,
                    extra,
                    mta_tax,
                    tip_amount,
                    tolls_amount,
                    improvement_surcharge,
                    total_amount,
                    congestion_surcharge,
                    EXTRACT(YEAR FROM lpep_pickup_datetime) AS year
                FROM read_parquet('{url}')
            """)
        logging.info(f"Inserted {url} into {service}_taxi_trip_data")
    except Exception as e:
        logging.error(f"FAILED {url} | {e}")

def run_pipeline():
    for year in range(START_YEAR, END_YEAR + 1):
        for month in MONTHS:
            for service in SERVICES:
                url = f"{BASE_URL}/{service}_tripdata_{year}-{month:02d}.parquet"
                logging.info(f"Downloading {url}")
                insert_parquet(url, service)

if __name__ == "__main__":
    logging.info(f"Starting pipeline from {START_YEAR} to {END_YEAR}")
    run_pipeline()
    logging.info("Pipeline finished.")