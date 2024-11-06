class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range (V)]

    def add_edge(self, u, v):
        self.adj[u].append((v))
        self.adj[v].append(u)

    def BFS(self):
        n = len(self.adj)
        visited = [False] * n
        Q = []

        source = 0
        print(source,end="\t")
        visited[source] = True
        Q.append(source)

        while Q != []:
            u = Q.pop(0)

            for v in self.adj[u]:
                if not visited[v]:
                    print(v,end="\t")
                    visited[v] = True
                    Q.append(v)


V = 7
G = Graph(V)

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(0,3)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(4,6)
print("\n Breadth First Search traversal gives--\n")
G.BFS()