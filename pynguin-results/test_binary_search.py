# Automatically generated by Pynguin.
import pytest
import binary_search as module_0

def test_case_0():
    int_0 = -990
    list_0 = [int_0, int_0, int_0, int_0]
    int_1 = 338
    bool_0 = module_0.binary_search(list_0, int_1)
    assert bool_0 is False

def test_case_1():
    list_0 = []
    int_0 = -401
    bool_0 = module_0.binary_search(list_0, int_0)
    assert bool_0 is False

@pytest.mark.xfail
def test_case_2():
    int_0 = -119
    list_0 = [int_0]
    bool_0 = module_0.binary_search(list_0, int_0)
    assert bool_0 is True
    none_type_0 = None
    int_1 = 296
    module_0.binary_search(none_type_0, int_1)

def test_case_3():
    float_0 = 2994.569025
    list_0 = [float_0]
    int_0 = 371
    bool_0 = module_0.binary_search(list_0, int_0)
    assert bool_0 is False
    int_1 = -1586
    bool_1 = module_0.binary_search(list_0, int_1)
    assert bool_1 is False