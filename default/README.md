# Math1234

This repository provides basic math operations (addition and subtraction) with automated testing using pytest.

## Folder Structure

- `src/`: Source code for math operations
- `tests/`: Pytest files for automated testing
- `default/requirements.txt`: Python dependencies
- `default/README.md`: Project usage and workflow instructions
- `default/math.json`: CI metadata for workflow generation

## Usage

1. Install dependencies:
   ```sh
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```sh
   python -m pytest tests/ -v --tb=short
   ```

## CI/CD Workflow

A CI pipeline is defined in `.github/workflows/ci.yml` (see `default/math.json` for metadata). It runs pytest on every push or pull request.
