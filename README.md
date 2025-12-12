# StackOverflow Data Analysis

A simple data analysis project for StackOverflow questions, answers, and tags.

## What It Does

Analyzes StackOverflow data to find:
- Question volume trends by year
- Average question scores and response times
- Answer rates over time
- Top questions by tags (Python, JavaScript, etc.)
- Most popular questions overall

## Requirements

```bash
pip install -r requirements.txt
```

Main dependencies: `pandas`, `pyspark`

## Data Files

Place these CSV files in the `data/` folder:
- `Questions.csv`
- `Answers.csv`
- `Tags.csv`

## How to Run

```bash
python test_spark.py
```

## Output

The script provides:
- Yearly analysis (2008 onwards)
- Top questions by tag
- Response time statistics
- Year-over-year comparisons
