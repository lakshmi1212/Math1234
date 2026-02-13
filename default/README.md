# Math1234

This repository contains basic math operations and their tests.

## Structure
- `src/math_operations.py`: Production code for addition and subtraction.
- `tests/test_add.py`: Tests for addition functionality.
- `tests/test_subtract.py`: Tests for subtraction functionality.
- `default/requirements.txt`: Python dependencies.
- `default/math.json`: CI/CD metadata for workflow generation.

## Usage

Install requirements:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/
```

## CI Workflow

The repository is ready for GitHub Actions CI using Python and pytest.
