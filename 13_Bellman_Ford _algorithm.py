class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append(Edge(u, v, weight))

    def bellman_ford(self, source):
        distance = [float('inf')] * self.V
        distance[source] = 0

        for _ in range(self.V - 1):
            for edge in self.edges:
                if distance[edge.u] != float('inf') and distance[edge.u] + edge.weight < distance[edge.v]:
                    distance[edge.v] = distance[edge.u] + edge.weight

        for edge in self.edges:
            if distance[edge.u] != float('inf') and distance[edge.u] + edge.weight < distance[edge.v]:
                print("Graph contains a negative weight cycle")
                return None

        return distance

graph = Graph(5)
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(3, 1, 1)
graph.add_edge(3, 2, 5)
graph.add_edge(4, 3, -3)

source_vertex = 0
distances = graph.bellman_ford(source_vertex)

if distances is not None:
    print("Vertex Distance from Source")
    for i in range(len(distances)):
        print(f"{i}\t\t{distances[i]}")
