import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3

def test_subtract_negative_numbers():
    assert subtract(-2, -3) == 1

def test_subtract_zero():
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0

def test_subtract_floats():
    assert subtract(5.6, 2.1) == pytest.approx(3.5)

def test_subtract_large_numbers():
    assert subtract(10**10, 10**9) == 9 * 10**9
