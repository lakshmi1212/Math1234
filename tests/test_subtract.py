import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (0, 0, 0),
    (-1, -1, 0),
    (5, -5, 10),
    (2.5, 1.5, 1.0),
    (1e10, 1, 1e10-1),
    (987654321, 123456789, 864197532),
])
def test_subtract_various(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract('1', 2)
