from algebra.min2 import min2

def test_min2():
    assert min2([4, 1, 2, 3]) == 2
    assert min2([7, 314]) == 314
    assert min2([-4, 0, 77, 42]) == 0
