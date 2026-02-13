# Math Operations

This repository provides basic math operations (addition and subtraction) with comprehensive testing and CI/CD integration.

## Folder Structure

- `src/`: Source code for math operations
- `tests/`: Pytest-based test cases
- `default/requirements.txt`: Python dependencies
- `default/README.md`: Project overview and instructions

## Usage

```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/ -v --tb=short
```

## CI/CD

A GitHub Actions workflow is expected at `.github/workflows/ci.yml` to run tests on push and pull request events.

_Last updated: 2024-06-12_
