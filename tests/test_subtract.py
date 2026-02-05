import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3

def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8
    assert subtract(-4, 7) == -11

def test_subtract_large_numbers():
    assert subtract(1000000, 999999) == 1
