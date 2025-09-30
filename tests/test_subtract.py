from calculator import subtract

def test_subtract_basic():
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    assert subtract(3, 5) == -2

def test_subtract_floats():
    assert subtract(5.5, 0.5) == 5.0
