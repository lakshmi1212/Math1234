import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_positive_and_negative():
    assert add(5, -3) == 2
    assert add(-4, 7) == 3

def test_add_large_numbers():
    assert add(1000000, 999999) == 1999999
