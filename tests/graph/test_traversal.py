from graph.traversal.bfs import bfs_2list
from tests.graph.sample import g_connected


def test_bfs_2list(g_connected):
    tree = bfs_2list(0, g_connected)
    assert set(tree.vertices()) == {0, 1, 3, 5}
    assert set(tree[1]) == {5}
    assert tree.pred(1) == 0
    assert tree.pred(0) is None
