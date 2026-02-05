# Math1234

This repository provides basic math operations (addition and subtraction) as Python functions, along with comprehensive pytest-based tests and CI workflow integration guidance.

## Usage

```
from src.math_operations import add, subtract

result1 = add(2, 3)         # 5
result2 = subtract(5, 2)    # 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/ -v --tb=short
```

## Continuous Integration

- Workflow file: `.github/workflows/ci.yml`
- Python version: 3.10
- Test command: `pytest tests/ -v --tb=short`
- Requirements: `default/requirements.txt`

## Folder Structure

- `src/` - Source code for math operations
- `tests/` - Pytest files for addition and subtraction
- `default/requirements.txt` - Python dependencies
- `default/README.md` - Project documentation
- `default/math.json` - CI workflow metadata
