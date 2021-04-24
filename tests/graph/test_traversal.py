from graph.traversal.bfs import bfs, bfs_2list
from tests.graph.sample import g_directed

def test_bfs(g_directed):
    for f in bfs, bfs_2list:
        tree = bfs(0, g_directed)
        assert set(tree.vertices()) == {0, 1, 3, 5}
        assert set(tree[1]) == {5}
        assert tree.pred(1) == 0
        assert tree.pred(0) is None
