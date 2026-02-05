import pytest
from src.math_operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
    (1e10, 1, 1e10+1),
    (123456789, 987654321, 1111111110),
])
def test_add_various(a, b, expected):
    assert add(a, b) == expected

def test_add_type_error():
    with pytest.raises(TypeError):
        add('1', 2)
