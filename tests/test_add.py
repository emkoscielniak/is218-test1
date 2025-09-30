from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_with_negatives():
    assert add(-5, 2) == -3

def test_add_floats():
    assert add(2.5, 0.5) == 3.0