# Math1234

This project provides basic math operations (addition and subtraction) with comprehensive pytest-based tests and CI integration.

## Usage

```
from src.math_operations import add, subtract

result_add = add(3, 2)        # 5
result_sub = subtract(3, 2)   # 1
```

## Testing

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/ -v --tb=short
```

## CI/CD

A GitHub Actions workflow is expected at `.github/workflows/ci.yml` to run all tests on push and pull requests.
