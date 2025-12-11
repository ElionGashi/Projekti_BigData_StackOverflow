"""
Data ingestion script - Load data from various sources
"""
import pandas as pd
from pyspark.sql import SparkSession
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, SPARK_CONFIG
from utils.logger import setup_logger

logger = setup_logger(__name__)


def create_spark_session() -> SparkSession:
    """
    Create and configure Spark session.
    
    Returns:
        SparkSession instance
    """
    logger.info("Creating Spark session...")
    spark = SparkSession.builder
    
    for key, value in SPARK_CONFIG.items():
        spark = spark.config(key, value)
    
    return spark.getOrCreate()


def load_csv_pandas(file_path: str) -> pd.DataFrame:
    """
    Load CSV file using Pandas.
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        Pandas DataFrame
    """
    logger.info(f"Loading CSV file with Pandas: {file_path}")
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully loaded {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Error loading CSV: {e}")
        raise


def load_csv_spark(spark: SparkSession, file_path: str):
    """
    Load CSV file using Spark.
    
    Args:
        spark: SparkSession instance
        file_path: Path to CSV file
        
    Returns:
        Spark DataFrame
    """
    logger.info(f"Loading CSV file with Spark: {file_path}")
    try:
        df = spark.read.csv(file_path, header=True, inferSchema=True)
        logger.info(f"Successfully loaded {df.count()} rows")
        return df
    except Exception as e:
        logger.error(f"Error loading CSV: {e}")
        raise


def save_data(df, output_path: str, format: str = "parquet"):
    """
    Save DataFrame to disk.
    
    Args:
        df: DataFrame (Pandas or Spark)
        output_path: Output file path
        format: Output format (parquet, csv, etc.)
    """
    logger.info(f"Saving data to {output_path} in {format} format")
    try:
        if isinstance(df, pd.DataFrame):
            if format == "parquet":
                df.to_parquet(output_path, index=False)
            elif format == "csv":
                df.to_csv(output_path, index=False)
        else:  # Spark DataFrame
            if format == "parquet":
                df.write.parquet(output_path, mode="overwrite")
            elif format == "csv":
                df.write.csv(output_path, header=True, mode="overwrite")
        logger.info("Data saved successfully")
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        raise


def main():
    """
    Main execution function
    """
    logger.info("Starting data ingestion process...")
    
    # Example usage - uncomment when you have data files
    # spark = create_spark_session()
    # df = load_csv_spark(spark, str(RAW_DATA_DIR / "your_data.csv"))
    # save_data(df, str(PROCESSED_DATA_DIR / "processed_data.parquet"))
    # spark.stop()
    
    logger.info("Data ingestion completed!")


if __name__ == "__main__":
    main()
