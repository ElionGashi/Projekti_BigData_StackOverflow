# Setup Guide

This guide will help you set up the development environment for the Big Data project.

## Prerequisites

### Required Software

1. **Python 3.8 or higher**
   - Check version: `python --version`
   - Download from: https://www.python.org/downloads/

2. **Java 8 or higher** (for Apache Spark)
   - Check version: `java -version`
   - Download from: https://www.oracle.com/java/technologies/downloads/

3. **Git**
   - Check version: `git --version`
   - Download from: https://git-scm.com/downloads/

### Optional Software

- **Jupyter Notebook**: Installed via requirements.txt
- **IDE**: VS Code, PyCharm, or your preferred editor

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/ElionGashi/Big-Data-Project.git
cd Big-Data-Project
```

### 2. Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import pyspark; print(f'PySpark version: {pyspark.__version__}')"
python -c "import pandas; print(f'Pandas version: {pandas.__version__}')"
```

### 5. Environment Variables (Optional)

Create a `.env` file in the project root:

```env
# Database configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bigdata
DB_USER=your_username
DB_PASSWORD=your_password

# Spark configuration
SPARK_HOME=/path/to/spark
```

## Running the Project

### 1. Data Ingestion

```bash
python src/ingestion/load_data.py
```

### 2. Data Processing

```bash
python src/processing/process_data.py
```

### 3. Data Analysis

```bash
python src/analysis/analyze_data.py
```

### 4. Jupyter Notebooks

Start Jupyter:
```bash
jupyter notebook
```

Or JupyterLab:
```bash
jupyter lab
```

Navigate to the `notebooks/` directory and open the desired notebook.

## Spark Configuration

### Local Mode (Default)

The project is configured to run Spark in local mode by default. This is suitable for development and small datasets.

### Cluster Mode (Advanced)

To run on a Spark cluster, modify the `SPARK_CONFIG` in `src/utils/config.py`:

```python
SPARK_CONFIG = {
    "spark.app.name": "BigDataProject",
    "spark.master": "spark://master-node:7077",  # Your cluster URL
    "spark.executor.memory": "4g",
    "spark.driver.memory": "2g",
}
```

## Troubleshooting

### Issue: Java not found

**Solution**: Install Java and set `JAVA_HOME` environment variable:

```bash
# Find Java installation
which java

# Set JAVA_HOME (add to ~/.bashrc or ~/.zshrc)
export JAVA_HOME=/path/to/java
export PATH=$JAVA_HOME/bin:$PATH
```

### Issue: PySpark import error

**Solution**: Ensure Java is installed and accessible:

```bash
java -version
```

### Issue: Memory errors with Spark

**Solution**: Reduce memory allocation in `src/utils/config.py`:

```python
SPARK_CONFIG = {
    "spark.executor.memory": "1g",
    "spark.driver.memory": "1g",
}
```

### Issue: Module not found

**Solution**: Ensure virtual environment is activated and dependencies are installed:

```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Development Tips

1. **Always activate virtual environment** before working
2. **Use Jupyter notebooks** for exploration
3. **Run scripts from project root** to ensure proper imports
4. **Check logs** for debugging information
5. **Keep dependencies updated**: `pip list --outdated`

## Testing the Setup

Run this test script to verify everything works:

```python
# test_setup.py
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

print("Testing imports...")
print(f"✓ Pandas version: {pd.__version__}")
print(f"✓ NumPy version: {np.__version__}")

print("\nTesting Spark...")
spark = SparkSession.builder \
    .appName("SetupTest") \
    .master("local[*]") \
    .getOrCreate()

print(f"✓ Spark version: {spark.version}")

# Create test DataFrame
df = spark.createDataFrame([(1, "test"), (2, "data")], ["id", "value"])
print(f"✓ Spark DataFrame created with {df.count()} rows")

spark.stop()
print("\n✅ All tests passed! Setup is complete.")
```

Run the test:
```bash
python test_setup.py
```

## Next Steps

After setup is complete:

1. Review the [Project Overview](PROJECT_OVERVIEW.md)
2. Explore the sample notebooks in `notebooks/`
3. Add your data to `data/raw/`
4. Start with data ingestion scripts

## Getting Help

- Check the [documentation](docs/)
- Review code examples in `src/`
- Consult [Apache Spark documentation](https://spark.apache.org/docs/latest/)
- Refer to [Pandas documentation](https://pandas.pydata.org/docs/)
