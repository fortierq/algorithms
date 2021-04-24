
from graph.graph import Graph
from graph.tree import RootedTree


def bfs_2list(s, g: Graph) -> RootedTree:
    cur, next = [s], []
    t = RootedTree(s)
    while cur:
        u = cur.pop()
        for v in g[u]:
            if v not in t:
                next.append(v)
                t.add(u, v)
        if not cur:
            cur, next = next, []
    return t
