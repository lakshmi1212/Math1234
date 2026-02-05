# Math1234

This repository provides basic math operations (addition and subtraction) implemented in Python, along with comprehensive pytest-based test suites and CI/CD integration meta-data.

## Usage

- Source code is in `src/math_operations.py`
- Tests are in `tests/test_add.py` and `tests/test_subtract.py`
- Install dependencies: `pip install -r default/requirements.txt`
- Run tests: `python -m pytest tests/ -v --tb=short`

## CI/CD Workflow

- Workflow file: `.github/workflows/ci.yml`
- Uses Python 3.10 and pytest 8.0.0
- All meta-data for workflow generation is in `default/math.json`
