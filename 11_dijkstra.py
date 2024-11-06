from heapq import heappush, heappop

class Node:
    def __init__(self, V, distance):
        self.v = V
        self.dist = distance

    def __lt__(self, other):
        return self.dist < other.dist
    
def dijkstra(V, adj, S):
    known = [False] * V
    map = {}
    Q = []

    map[S] = Node(S, 0)
    heappush(Q, Node(S, 0))

    while Q:
        n = heappop(Q)
        v = n.v
        distance = n.dist

        if known[v]: 
            continue

        known[v] = True
        adjList = adj[v]

        for adjLink in adjList:
            neighbor, weight = adjLink
            if not known[neighbor]:
                new_dist = distance + weight
                if neighbor not in map or new_dist < map[neighbor].dist:
                    map[neighbor] = Node(v, new_dist)
                    heappush(Q, Node(neighbor, new_dist))

    result = [(map[i].v if i in map else -1, map[i].dist if i in map else float('inf')) for i in range(V)]
    return result

V = 6
E = 9
adj = [[] for _ in range(V)]
u = [0, 0, 0, 1, 2, 2, 3, 3, 4]
v = [1, 2, 3, 3, 4, 5, 2, 4, 5]
w = [3, 1, 2, 5, 7, 6, 4, 2, 1]

for i in range(E):
    adj[u[i]].append((v[i], w[i]))

Source = 0
result = dijkstra(V, adj, Source)
print(result)