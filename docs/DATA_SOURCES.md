# Data Sources

This document describes the data sources used in this project and how to access them.

## Overview

Document all data sources used in your project here. Include:
- Source name and description
- Access method
- Data format
- Update frequency
- License/terms of use

## Example Data Sources

### 1. Public Datasets

#### Kaggle Datasets
- **URL**: https://www.kaggle.com/datasets
- **Access**: Download via Kaggle API or web interface
- **Formats**: CSV, JSON, Parquet
- **License**: Varies by dataset

#### UCI Machine Learning Repository
- **URL**: https://archive.ics.uci.edu/ml/index.php
- **Access**: Direct download
- **Formats**: CSV, ARFF
- **License**: Open for research

#### Google Dataset Search
- **URL**: https://datasetsearch.research.google.com/
- **Access**: Links to various sources
- **Formats**: Various
- **License**: Varies

### 2. Government Data

#### data.gov
- **URL**: https://data.gov/
- **Access**: Direct download or API
- **Formats**: CSV, JSON, XML
- **License**: Public domain

#### European Data Portal
- **URL**: https://data.europa.eu/
- **Access**: Direct download
- **Formats**: Various
- **License**: Varies

### 3. APIs

#### Example REST API
```python
import requests

url = "https://api.example.com/data"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get(url, headers=headers)
data = response.json()
```

### 4. Database Connections

#### PostgreSQL Example
```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="dbname",
    user="username",
    password="password"
)
```

#### MongoDB Example
```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['database_name']
collection = db['collection_name']
```

## Data Collection Guidelines

1. **Always check licensing** before using data
2. **Document data sources** with proper attribution
3. **Store raw data** in `data/raw/` directory
4. **Never commit large data files** to Git (add to .gitignore)
5. **Include data dictionaries** explaining fields
6. **Note collection date** for reproducibility

## Data Storage

- **Raw Data**: `data/raw/` - Original, unmodified data
- **Processed Data**: `data/processed/` - Cleaned and transformed data
- **External**: Consider cloud storage (S3, Azure Blob) for large datasets

## Sample Data

For testing purposes, you can generate sample data:

```python
import pandas as pd
import numpy as np

# Generate sample dataset
n_rows = 1000
df = pd.DataFrame({
    'id': range(n_rows),
    'value': np.random.randn(n_rows),
    'category': np.random.choice(['A', 'B', 'C'], n_rows),
    'timestamp': pd.date_range('2024-01-01', periods=n_rows, freq='h')
})

df.to_csv('data/raw/sample_data.csv', index=False)
```

## Data Ethics

- Ensure compliance with data privacy regulations (GDPR, CCPA)
- Remove or anonymize personal information
- Obtain necessary permissions for data use
- Follow institutional review board (IRB) requirements if applicable

## Adding New Data Sources

When adding a new data source:

1. Document it in this file
2. Add download/access scripts to `src/ingestion/`
3. Include data validation checks
4. Update README with any new requirements
5. Consider data versioning for reproducibility
