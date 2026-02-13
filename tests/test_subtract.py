import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_mixed_signs():
    assert subtract(-2, 3) == -5
    assert subtract(2, -3) == 5

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)
    assert subtract(-2.5, 2.5) == pytest.approx(-5.0)
