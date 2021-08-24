class Graph:
    def __init__(self, verticies, edges):
        self._edges = set(frozenset((u, v)) for u, v in edges)
        self._neighbours = {}
        for vertex in verticies:
            self._neighbours[vertex] = set()
        for u, v in self._edges:
            self.add_edge(u, v)

    def add_vertex(self, v):
        if v not in self._neighbours:
            self._neighbours[v] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self._edges.add(frozenset([u,v]))
        self._neighbours[u].add(v)
        self._neighbours[v].add(u)

    def degree(self, v):
        """Return number of edges incident to vertex"""
        return len(self._neighbours[v])

    def neighbours(self, v):
        return iter(self._neighbours[v])

    def remove_edge(self, u, v):
        e = frozenset([u, v])
        if e in self._edges:
            self._edges.remove(e)
            self._neighbours[u].remove(v)
            self._neighbours[v].remove(u)

    def remove_vertex(self, u):
        to_delete = list(self.neighbours(u))
        for v in to_delete:
            self.remove_edge(u, v)
        del self._neighbours[u]

    @property
    def m(self):
        return len(self._edges)

    @property
    def n(self):
        return len(self._neighbours)


if __name__ == '__main__':
    G = Graph({1, 2, 3}, {(1, 2), (2, 3)})

    assert(G.degree(1) == 1)
    assert(G.degree(2) == 2)
    assert(G.degree(3) == 1)

    assert(set(G.neighbours(2)) == {1, 3})

    G.remove_edge(1, 2)
    assert(G.n == 3 and G.m == 1)

    G.add_edge(1,2)
    assert(G.n == 3 and G.m == 2)

    G.remove_vertex(2)
    assert(G.n == 2 and G.m == 0)

    print('Still working...')
