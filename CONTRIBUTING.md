# Contributing to Big Data Project

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Issues

- Check if the issue already exists
- Use the issue tracker to report bugs
- Provide detailed information about the issue
- Include steps to reproduce the problem

### Submitting Changes

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Write clear, concise commit messages
   - Follow the code style guidelines
   - Add tests if applicable
4. **Test your changes**
   ```bash
   python -m pytest tests/
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add: description of your changes"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## 📝 Code Style Guidelines

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use type hints where appropriate

### Example:
```python
def process_data(input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Process and clean input data.
    
    Args:
        input_data: Raw data DataFrame
        
    Returns:
        Processed DataFrame
    """
    # Implementation
    return processed_data
```

### Commit Message Format

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Start with a capital letter
- Keep the subject line under 50 characters
- Add detailed description if needed

Examples:
- `Add data ingestion module for CSV files`
- `Fix: Handle missing values in preprocessing`
- `Update: Improve documentation for analysis scripts`

## 🧪 Testing

- Write unit tests for new features
- Ensure all tests pass before submitting PR
- Aim for good test coverage

## 📚 Documentation

- Update README.md if you change functionality
- Add docstrings to new functions and classes
- Update relevant documentation in the `docs/` folder

## 🔍 Code Review Process

1. All submissions require review
2. Reviewers will provide feedback
3. Address feedback and update PR
4. Once approved, changes will be merged

## ❓ Questions?

Feel free to open an issue for any questions or concerns.

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.
