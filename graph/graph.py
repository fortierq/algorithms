
class Graph:
    def __getitem__(self, v):
        raise NotImplementedError()
    def __contains__(self, v):
        raise NotImplementedError()
    def add(self, u, v):
        raise NotImplementedError()
    def edge(self, u, v):
        raise NotImplementedError()
    def vertices(self):
        raise NotImplementedError()
    