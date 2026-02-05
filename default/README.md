# Math1234

This repository provides basic math operations (addition and subtraction) with Python functions and corresponding pytest-based tests.

## Usage

```python
from src.math_operations import add, subtract

result = add(2, 3)        # Returns 5
result2 = subtract(5, 2)  # Returns 3
```

## Testing

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests:

```bash
python -m pytest tests/ -v --tb=short
```

## CI/CD Workflow

See `.github/workflows/ci.yml` for automated test execution on push and pull requests.
