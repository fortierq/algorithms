import pytest


@pytest.fixture
def g_directed():
    return {0: [1, 3], 1: [3, 5], 2: [4, 0], 3: [0], 4: [3], 5: []}

@pytest.fixture
def g_undirected():
    return {
        0: {1, 2}, 
        1: {0, 3, 4}, 
        2: {5, 0}, 
        3: {0, 1}, 
        4: {1}, 
        5: {2, 6},
        6: {2}
    }
