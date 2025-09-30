from calculator import multiply

def test_multiply_basic():
    assert multiply(4, 3) == 12

def test_multiply_by_zero():
    assert multiply(25, 0) == 0

def test_multiply_floats():
    assert multiply(2.5, 2.0) == 5.0
