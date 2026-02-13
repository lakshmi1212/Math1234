# Math Operations Library

This repository provides basic math operations (addition and subtraction) with production-ready test coverage and CI/CD integration guidance.

## Folder Structure

- `src/` — Source code for math operations (`math_operations.py`)
- `tests/` — Pytest test files for all operations
- `default/` — Project metadata and requirements

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 3))   # Output: 2
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

## CI/CD Workflow

- Workflow file location: `.github/workflows/ci.yml`
- Uses Python 3.10 and pytest
- Triggers on push and pull request to `main`

## License

MIT
