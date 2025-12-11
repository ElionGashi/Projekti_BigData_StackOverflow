# Quick Start Guide

Get started with the Big Data Project in minutes!

## 🚀 Quick Setup (5 minutes)

### 1. Clone and Setup

```bash
# Clone repository
git clone https://github.com/ElionGashi/Big-Data-Project.git
cd Big-Data-Project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify Installation

```bash
python -c "import pyspark; print('✓ PySpark installed')"
python -c "import pandas; print('✓ Pandas installed')"
```

## 📊 First Analysis (10 minutes)

### Option 1: Using Jupyter Notebook (Recommended)

```bash
# Start Jupyter
jupyter notebook

# Open: notebooks/01_data_exploration.ipynb
# Follow the examples in the notebook
```

### Option 2: Using Python Scripts

```bash
# Generate sample data
python -c "
import pandas as pd
import numpy as np

# Create sample dataset
np.random.seed(42)
df = pd.DataFrame({
    'id': range(1, 1001),
    'value': np.random.randn(1000) * 100 + 500,
    'category': np.random.choice(['A', 'B', 'C', 'D'], 1000),
    'date': pd.date_range('2024-01-01', periods=1000, freq='h')
})

df.to_csv('data/raw/sample_data.csv', index=False)
print('✓ Sample data created: data/raw/sample_data.csv')
"

# Run quick analysis
python -c "
import pandas as pd

# Load data
df = pd.read_csv('data/raw/sample_data.csv')

# Quick analysis
print('Dataset Shape:', df.shape)
print('\nFirst 5 rows:')
print(df.head())
print('\nStatistics:')
print(df.describe())
print('\nCategory Counts:')
print(df['category'].value_counts())
"
```

## 🔥 Common Tasks

### Load Data with Pandas

```python
import pandas as pd

# Load CSV
df = pd.read_csv('data/raw/your_data.csv')

# Quick look
print(df.head())
print(df.info())
print(df.describe())
```

### Load Data with Spark

```python
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("QuickStart") \
    .master("local[*]") \
    .getOrCreate()

# Load data
df = spark.read.csv('data/raw/your_data.csv', header=True, inferSchema=True)

# Show data
df.show(5)
df.printSchema()
df.describe().show()

# Stop session
spark.stop()
```

### Basic Data Cleaning

```python
import pandas as pd

df = pd.read_csv('data/raw/your_data.csv')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna()  # or df.fillna(0)

# Save cleaned data
df.to_csv('data/processed/cleaned_data.csv', index=False)
```

### Simple Visualization

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/raw/sample_data.csv')

# Distribution plot
df['value'].hist(bins=30)
plt.title('Value Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('output/distribution.png')
plt.show()

# Box plot by category
df.boxplot(column='value', by='category')
plt.title('Value by Category')
plt.suptitle('')
plt.savefig('output/boxplot.png')
plt.show()
```

## 📁 Project Structure at a Glance

```
Big-Data-Project/
├── data/
│   ├── raw/          → Put your raw data here
│   └── processed/    → Processed data goes here
├── notebooks/        → Jupyter notebooks for exploration
├── src/              → Python source code
│   ├── ingestion/    → Data loading scripts
│   ├── processing/   → Data cleaning scripts
│   └── analysis/     → Analysis scripts
├── output/           → Generated reports and figures
└── docs/             → Documentation
```

## 🎯 Next Steps

1. **Add Your Data**: Place your data files in `data/raw/`
2. **Explore**: Open Jupyter notebooks in `notebooks/`
3. **Customize**: Modify scripts in `src/` for your needs
4. **Document**: Update docs with your findings

## 📚 Learn More

- [Full Setup Guide](docs/SETUP_GUIDE.md)
- [Project Overview](docs/PROJECT_OVERVIEW.md)
- [Methodology](docs/METHODOLOGY.md)
- [Data Sources](docs/DATA_SOURCES.md)

## 💡 Tips

- **Use make commands**: `make install`, `make notebook`, `make test`
- **Virtual environment**: Always activate before working
- **Jupyter shortcuts**: Press `h` in Jupyter for keyboard shortcuts
- **Git**: Commit often with clear messages

## ❓ Common Issues

**Import errors?**
```bash
# Make sure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**Java not found for Spark?**
```bash
# Install Java 8+
java -version
```

**Out of memory?**
- Reduce data size for testing
- Use Spark for large datasets
- Adjust memory settings in config

## 🎓 Learning Resources

- [PySpark Tutorial](https://spark.apache.org/docs/latest/api/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

**Ready to start?** Open Jupyter and start exploring! 🚀

```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```
