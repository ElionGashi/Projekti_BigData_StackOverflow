"""
Data processing script - Clean and transform data
"""
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.config import PROCESSED_DATA_DIR
from utils.logger import setup_logger

logger = setup_logger(__name__)


def clean_missing_values(df, strategy: str = "drop"):
    """
    Handle missing values in DataFrame.
    
    Args:
        df: Input DataFrame (Pandas or Spark)
        strategy: Strategy for handling missing values ('drop', 'fill')
        
    Returns:
        Cleaned DataFrame
    """
    logger.info(f"Cleaning missing values with strategy: {strategy}")
    
    if isinstance(df, pd.DataFrame):
        if strategy == "drop":
            return df.dropna()
        elif strategy == "fill":
            return df.fillna(df.mean(numeric_only=True))
    else:  # Spark DataFrame
        if strategy == "drop":
            return df.dropna()
        elif strategy == "fill":
            numeric_cols = [f.name for f in df.schema.fields 
                          if str(f.dataType) in ['IntegerType', 'DoubleType', 'FloatType']]
            for col in numeric_cols:
                mean_val = df.select(F.mean(col)).first()[0]
                df = df.fillna({col: mean_val})
            return df
    
    return df


def remove_duplicates(df):
    """
    Remove duplicate rows from DataFrame.
    
    Args:
        df: Input DataFrame (Pandas or Spark)
        
    Returns:
        DataFrame without duplicates
    """
    logger.info("Removing duplicate rows")
    
    if isinstance(df, pd.DataFrame):
        return df.drop_duplicates()
    else:  # Spark DataFrame
        return df.dropDuplicates()


def normalize_column_names(df):
    """
    Normalize column names (lowercase, replace spaces with underscores).
    
    Args:
        df: Input DataFrame (Pandas or Spark)
        
    Returns:
        DataFrame with normalized column names
    """
    logger.info("Normalizing column names")
    
    if isinstance(df, pd.DataFrame):
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        return df
    else:  # Spark DataFrame
        for col in df.columns:
            new_col = col.lower().replace(' ', '_')
            df = df.withColumnRenamed(col, new_col)
        return df


def filter_outliers(df, column: str, n_std: float = 3.0):
    """
    Filter outliers using standard deviation method.
    
    Args:
        df: Input DataFrame (Pandas or Spark)
        column: Column name to check for outliers
        n_std: Number of standard deviations for threshold
        
    Returns:
        Filtered DataFrame
    """
    logger.info(f"Filtering outliers in column: {column}")
    
    if isinstance(df, pd.DataFrame):
        mean = df[column].mean()
        std = df[column].std()
        df = df[(df[column] >= mean - n_std * std) & (df[column] <= mean + n_std * std)]
        return df
    else:  # Spark DataFrame
        stats = df.select(F.mean(column), F.stddev(column)).first()
        mean, std = stats[0], stats[1]
        df = df.filter(
            (F.col(column) >= mean - n_std * std) & 
            (F.col(column) <= mean + n_std * std)
        )
        return df


def main():
    """
    Main execution function
    """
    logger.info("Starting data processing...")
    
    # Example usage - uncomment when you have data
    # spark = SparkSession.builder.appName("DataProcessing").getOrCreate()
    # df = spark.read.parquet(str(PROCESSED_DATA_DIR / "processed_data.parquet"))
    # 
    # # Apply transformations
    # df = normalize_column_names(df)
    # df = remove_duplicates(df)
    # df = clean_missing_values(df, strategy="fill")
    # 
    # # Save processed data
    # df.write.parquet(str(PROCESSED_DATA_DIR / "cleaned_data.parquet"), mode="overwrite")
    # spark.stop()
    
    logger.info("Data processing completed!")


if __name__ == "__main__":
    main()
