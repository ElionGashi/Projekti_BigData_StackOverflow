"""
Data analysis script - Perform statistical analysis and generate insights
"""
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.config import PROCESSED_DATA_DIR, OUTPUT_DIR
from utils.logger import setup_logger

logger = setup_logger(__name__)

# Set plot style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)


def descriptive_statistics(df):
    """
    Calculate descriptive statistics for DataFrame.
    
    Args:
        df: Input DataFrame (Pandas or Spark)
        
    Returns:
        Statistics DataFrame
    """
    logger.info("Calculating descriptive statistics")
    
    if isinstance(df, pd.DataFrame):
        return df.describe()
    else:  # Spark DataFrame
        return df.describe()


def correlation_analysis(df):
    """
    Perform correlation analysis on numeric columns.
    
    Args:
        df: Input DataFrame (Pandas)
        
    Returns:
        Correlation matrix
    """
    logger.info("Performing correlation analysis")
    
    if isinstance(df, pd.DataFrame):
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].corr()
    else:
        logger.warning("Convert Spark DataFrame to Pandas for correlation analysis")
        return None


def plot_distributions(df, columns: list, output_path: str = None):
    """
    Plot distribution of specified columns.
    
    Args:
        df: Input DataFrame (Pandas)
        columns: List of column names to plot
        output_path: Optional path to save the plot
    """
    logger.info(f"Plotting distributions for columns: {columns}")
    
    if isinstance(df, pd.DataFrame):
        n_cols = len(columns)
        fig, axes = plt.subplots(1, n_cols, figsize=(6*n_cols, 5))
        
        if n_cols == 1:
            axes = [axes]
        
        for idx, col in enumerate(columns):
            df[col].hist(bins=30, ax=axes[idx], edgecolor='black')
            axes[idx].set_title(f'Distribution of {col}')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Frequency')
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            logger.info(f"Plot saved to {output_path}")
        else:
            plt.show()
        
        plt.close()


def plot_correlation_heatmap(corr_matrix, output_path: str = None):
    """
    Plot correlation heatmap.
    
    Args:
        corr_matrix: Correlation matrix
        output_path: Optional path to save the plot
    """
    logger.info("Plotting correlation heatmap")
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Heatmap', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        logger.info(f"Heatmap saved to {output_path}")
    else:
        plt.show()
    
    plt.close()


def group_analysis(df, group_col: str, agg_col: str, agg_func: str = "mean"):
    """
    Perform group-by analysis.
    
    Args:
        df: Input DataFrame (Pandas or Spark)
        group_col: Column to group by
        agg_col: Column to aggregate
        agg_func: Aggregation function (mean, sum, count, etc.)
        
    Returns:
        Grouped DataFrame
    """
    logger.info(f"Performing group analysis: {group_col} -> {agg_col} ({agg_func})")
    
    if isinstance(df, pd.DataFrame):
        if agg_func == "mean":
            return df.groupby(group_col)[agg_col].mean()
        elif agg_func == "sum":
            return df.groupby(group_col)[agg_col].sum()
        elif agg_func == "count":
            return df.groupby(group_col)[agg_col].count()
    else:  # Spark DataFrame
        if agg_func == "mean":
            return df.groupBy(group_col).agg(F.mean(agg_col))
        elif agg_func == "sum":
            return df.groupBy(group_col).agg(F.sum(agg_col))
        elif agg_func == "count":
            return df.groupBy(group_col).agg(F.count(agg_col))
    
    return None


def main():
    """
    Main execution function
    """
    logger.info("Starting data analysis...")
    
    # Example usage - uncomment when you have data
    # df = pd.read_parquet(PROCESSED_DATA_DIR / "cleaned_data.parquet")
    # 
    # # Descriptive statistics
    # stats = descriptive_statistics(df)
    # print(stats)
    # 
    # # Correlation analysis
    # corr = correlation_analysis(df)
    # if corr is not None:
    #     plot_correlation_heatmap(corr, OUTPUT_DIR / "correlation_heatmap.png")
    # 
    # # Distribution plots
    # numeric_cols = df.select_dtypes(include=[np.number]).columns[:3]
    # plot_distributions(df, numeric_cols, OUTPUT_DIR / "distributions.png")
    
    logger.info("Data analysis completed!")


if __name__ == "__main__":
    main()
