"""
Generate sample data for testing and demonstration purposes
"""
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.config import RAW_DATA_DIR
from utils.logger import setup_logger

logger = setup_logger(__name__)


def generate_sales_data(n_rows: int = 10000) -> pd.DataFrame:
    """
    Generate sample sales data.
    
    Args:
        n_rows: Number of rows to generate
        
    Returns:
        DataFrame with sales data
    """
    logger.info(f"Generating {n_rows} rows of sales data")
    
    np.random.seed(42)
    
    df = pd.DataFrame({
        'transaction_id': range(1, n_rows + 1),
        'date': pd.date_range('2023-01-01', periods=n_rows, freq='h'),
        'product_id': np.random.randint(1, 100, n_rows),
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books', 'Toys'], n_rows),
        'quantity': np.random.randint(1, 10, n_rows),
        'price': np.random.uniform(5.0, 500.0, n_rows).round(2),
        'customer_id': np.random.randint(1, 1000, n_rows),
        'store_id': np.random.randint(1, 20, n_rows),
        'payment_method': np.random.choice(['Credit Card', 'Cash', 'Debit Card', 'PayPal'], n_rows),
        'discount_percent': np.random.choice([0, 5, 10, 15, 20], n_rows),
    })
    
    # Calculate total amount
    df['total_amount'] = (df['price'] * df['quantity'] * (1 - df['discount_percent'] / 100)).round(2)
    
    # Add some missing values randomly
    missing_mask = np.random.random(n_rows) < 0.05
    df.loc[missing_mask, 'discount_percent'] = np.nan
    
    return df


def generate_user_data(n_rows: int = 1000) -> pd.DataFrame:
    """
    Generate sample user/customer data.
    
    Args:
        n_rows: Number of rows to generate
        
    Returns:
        DataFrame with user data
    """
    logger.info(f"Generating {n_rows} rows of user data")
    
    np.random.seed(42)
    
    df = pd.DataFrame({
        'user_id': range(1, n_rows + 1),
        'age': np.random.randint(18, 80, n_rows),
        'gender': np.random.choice(['M', 'F', 'Other'], n_rows),
        'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], n_rows),
        'registration_date': pd.date_range('2020-01-01', periods=n_rows, freq='D'),
        'total_purchases': np.random.randint(0, 100, n_rows),
        'total_spent': np.random.uniform(0, 5000, n_rows).round(2),
        'is_premium': np.random.choice([True, False], n_rows, p=[0.2, 0.8]),
    })
    
    return df


def generate_sensor_data(n_rows: int = 50000) -> pd.DataFrame:
    """
    Generate sample IoT sensor data.
    
    Args:
        n_rows: Number of rows to generate
        
    Returns:
        DataFrame with sensor data
    """
    logger.info(f"Generating {n_rows} rows of sensor data")
    
    np.random.seed(42)
    
    df = pd.DataFrame({
        'timestamp': pd.date_range('2024-01-01', periods=n_rows, freq='min'),
        'sensor_id': np.random.randint(1, 10, n_rows),
        'temperature': np.random.normal(25, 5, n_rows).round(2),
        'humidity': np.random.normal(60, 10, n_rows).clip(0, 100).round(2),
        'pressure': np.random.normal(1013, 10, n_rows).round(2),
        'status': np.random.choice(['active', 'idle', 'maintenance'], n_rows, p=[0.7, 0.2, 0.1]),
    })
    
    return df


def generate_log_data(n_rows: int = 100000) -> pd.DataFrame:
    """
    Generate sample application log data.
    
    Args:
        n_rows: Number of rows to generate
        
    Returns:
        DataFrame with log data
    """
    logger.info(f"Generating {n_rows} rows of log data")
    
    np.random.seed(42)
    
    df = pd.DataFrame({
        'timestamp': pd.date_range('2024-01-01', periods=n_rows, freq='s'),
        'level': np.random.choice(['INFO', 'WARNING', 'ERROR', 'DEBUG'], n_rows, p=[0.7, 0.15, 0.1, 0.05]),
        'user_id': np.random.randint(1, 1000, n_rows),
        'endpoint': np.random.choice(['/api/login', '/api/data', '/api/profile', '/api/search'], n_rows),
        'response_time_ms': np.random.exponential(100, n_rows).round(2),
        'status_code': np.random.choice([200, 201, 400, 404, 500], n_rows, p=[0.8, 0.05, 0.08, 0.05, 0.02]),
    })
    
    return df


def main():
    """
    Main function to generate all sample datasets
    """
    logger.info("Starting sample data generation...")
    
    try:
        # Generate sales data
        sales_df = generate_sales_data(10000)
        sales_path = RAW_DATA_DIR / "sample_sales.csv"
        sales_df.to_csv(sales_path, index=False)
        logger.info(f"✓ Sales data saved to {sales_path}")
        
        # Generate user data
        user_df = generate_user_data(1000)
        user_path = RAW_DATA_DIR / "sample_users.csv"
        user_df.to_csv(user_path, index=False)
        logger.info(f"✓ User data saved to {user_path}")
        
        # Generate sensor data
        sensor_df = generate_sensor_data(50000)
        sensor_path = RAW_DATA_DIR / "sample_sensors.csv"
        sensor_df.to_csv(sensor_path, index=False)
        logger.info(f"✓ Sensor data saved to {sensor_path}")
        
        # Generate log data
        log_df = generate_log_data(100000)
        log_path = RAW_DATA_DIR / "sample_logs.csv"
        log_df.to_csv(log_path, index=False)
        logger.info(f"✓ Log data saved to {log_path}")
        
        logger.info("✅ All sample data generated successfully!")
        
        # Print summary
        print("\n" + "="*60)
        print("SAMPLE DATA GENERATION COMPLETE")
        print("="*60)
        print(f"Sales data:  {len(sales_df):,} rows → {sales_path}")
        print(f"User data:   {len(user_df):,} rows → {user_path}")
        print(f"Sensor data: {len(sensor_df):,} rows → {sensor_path}")
        print(f"Log data:    {len(log_df):,} rows → {log_path}")
        print("="*60)
        
    except Exception as e:
        logger.error(f"Error generating sample data: {e}")
        raise


if __name__ == "__main__":
    main()
