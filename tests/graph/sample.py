import pytest


@pytest.fixture
def g_connected():
    return {0: [1, 3], 1: [3, 5], 2: [4, 0], 3: [0], 4: [3], 5: []}
