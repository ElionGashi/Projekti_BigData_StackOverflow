.PHONY: help install test clean run-ingest run-process run-analyze notebook

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Clean temporary files"
	@echo "  make run-ingest   - Run data ingestion"
	@echo "  make run-process  - Run data processing"
	@echo "  make run-analyze  - Run data analysis"
	@echo "  make notebook     - Start Jupyter notebook"
	@echo "  make lint         - Run code linting"

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf build/ dist/

run-ingest:
	python src/ingestion/load_data.py

run-process:
	python src/processing/process_data.py

run-analyze:
	python src/analysis/analyze_data.py

notebook:
	jupyter notebook notebooks/

lint:
	@echo "Running flake8..."
	@pip show flake8 > /dev/null 2>&1 || pip install flake8
	flake8 src/ --max-line-length=100 --exclude=__pycache__

format:
	@echo "Running black..."
	@pip show black > /dev/null 2>&1 || pip install black
	black src/ tests/
