from collections import deque

from graph.graph import Graph
from graph.tree import RootedTree


def bfs(s, g: Graph) -> RootedTree:
    q = deque([s])
    t = RootedTree(s)
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in t:
                q.append(v)
                t.add(u, v)
    return t

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
