from graph.connectivity.bridge import tarjan
from tests.graph.sample import g_undirected

def test_tarjan(g_undirected):
    bridges = tarjan(g_undirected)
    assert len(bridges) == 2
    assert (0, 2) in bridges or (2, 0) in bridges
    assert (1, 4) in bridges or (4, 1) in bridges
