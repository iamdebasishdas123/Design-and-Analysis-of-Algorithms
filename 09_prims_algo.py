import heapq as hp

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range (V)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v,w))
        self.adj[v].append((u,w))

    def Prim(self):
        pq = []
        source = 0
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        in_mst = [False] * self.V

        hp.heappush(pq,(0, source))
        key[source] = 0
        cost = 0

        while pq:
            u = hp.heappop(pq)[1]

            if in_mst[u]:
                continue
            in_mst[u] = True
            cost += key[u]


            for v,weight in self.adj[u]:
                if not in_mst[v] and key[v] > weight:
                    key[v] = weight
                    hp.heappush(pq,(key[v], v))
                    parent[v] = u

        for i in range(1, self.V):
            print(f"{parent[i]} -- {i} with weight {key[i]}")
        print(f"Total Cost : {cost}")


V = 7
G = Graph(V)

G.add_edge(0,1,28)
G.add_edge(0,5,10)
G.add_edge(5,4,25)
G.add_edge(4,6,24)
G.add_edge(6,1,14)
G.add_edge(1,2,16)
G.add_edge(2,3,12)
G.add_edge(3,6,18)
G.add_edge(3,4,22)

G.Prim()