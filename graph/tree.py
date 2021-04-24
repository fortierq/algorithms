from graph.graph import Graph
from collections import defaultdict


class RootedTree(Graph):
    def __init__(self, root):
        self._pred = dict()
        self._next = defaultdict(set)
        self._root = root
    def __getitem__(self, v):
        yield from self._next[v]
    def add(self, v, w):
        self._next[v].add(w)
        self._pred[w] = v
    def edge(self, u, v):
        return v in self._next[u]
    def __contains__(self, e):
        return e == self._root or e in self._pred
    def vertices(self):
        yield self._root
        yield from self._pred
    def pred(self, v):
        return self._pred.get(v, None)
