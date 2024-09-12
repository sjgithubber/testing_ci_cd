from src.math_ops import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(1, -1) == 0
    assert add(-2, 23) == 21

def test_sub():
    assert sub(1, -1) == 2
    assert sub(9,1) == 8
    assert sub(19, -2) == 21