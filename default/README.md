# Math1234

This repository implements basic mathematical operations (addition and subtraction) in Python, with automated tests and a CI workflow.

## Usage

- Source code: `src/math_operations.py`
- Tests: `tests/test_add.py`, `tests/test_subtract.py`

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests:

```bash
pytest tests/ -v --tb=short
```

## CI/CD Workflow

See `.github/workflows/ci.yml` for automated test execution on push and pull request events.
