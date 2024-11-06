class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def is_cycle_bfs(self):
        visited = [False] * self.V
        parent = [-1] * self.V

        for source in range(self.V):
            if not visited[source]:
                if self.bfs_cycle(source, visited, parent):
                    return True
        return False

    def bfs_cycle(self, source, visited, parent):
        queue = []

        visited[source] = True
        queue.append(source)

        while queue:
            u = queue.pop(0)

            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:
                    return True
        return False


V = 7
G = Graph(V)

G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(0, 3)
# G.add_edge(1, 3)
# G.add_edge(2, 3)
# G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)

if G.is_cycle_bfs():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")