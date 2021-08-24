class Graph:
    """Representation of a graph using an adjacency map"""

    # --- Nested vertex class:
    class Vertex:
        """Vertex structure for a graph"""

        def __init__(self, x):
            """Dont call constuctor directly, use Graphs insert_vertex(x)"""
            self._element = x

        def elemenet(self):
            """Return element associated with this vertex"""
            return self._elemenet

        def __hash__(self):  # allows verted to be a map/set key
            return hash(id(self))

    # --- nested Edge class:
    class Edge:
        """Edge structure for a graph"""

        def __init__(self, u, v, x):
            """Dontt call constructor directly, use graphs indset_edge(u,v,x)"""
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            """Return (u,v) tuple for verticies u and v"""
            return (self._origin, self._destination)

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge"""
            return self._destination if v is self._origin else self._origin

        def element(self):
            """Return element associated with this edge"""
            return self._element

        def __hash__(self):  # allows edge to be a map/set key
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        """Create empty graph, undirencted by default.
        Graph directed if optional parameter set to True.
        """
        self._outgoing = {}
        # only create second map for directed graph: use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return True if this is a directed graph, False if not.
        Property based on initial declaration of graph, not its contents
        """
        return self._incoming is not self._outgoing  # directed if maps are distinct

    def vertex_count(self):
        """Return the number of verticies in the graph"""
        return len(self._outgoing)

    def verticies(self):
        """Return an iteration of all the verticies of the graph"""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph"""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not ot double count edges:
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all the edges of the graph"""
        result = set()  # avoids double reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            # add edges to resulting set:
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent"""
        return self._outgoing[u].get(v)  # returns none if v not adjacent

    def degree(self, v, outgoing=True):
        """Return number of (outgoing) edges incidnet to vertex v in graph.
        If graph is directed, optional param used to request incoming edges
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed optional param used to request incoming edges."""
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values:
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self._Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x"""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        