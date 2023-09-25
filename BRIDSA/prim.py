import sys

def prim(graph):
    visited = set()
    start_vertex = input("Enter the starting vertex: ")
    visited.add(start_vertex)

    minimum_spanning_tree = []
    total_weight = 0

    while len(visited) < len(graph):
        min_edge = None

        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited and (min_edge is None or weight < min_edge[2]):
                    min_edge = (vertex, neighbor, weight)

        if min_edge:
            source, target, weight = min_edge
            visited.add(target)
            minimum_spanning_tree.append((source, target, weight))
            total_weight += weight

    return minimum_spanning_tree, total_weight

# Input the graph as an adjacency list
graph = {}

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    source, target, weight = input("Enter edge (source target weight): ").split()
    weight = int(weight)

    if source not in graph:
        graph[source] = []
    if target not in graph:
        graph[target] = []

    graph[source].append((target, weight))
    graph[target].append((source, weight))

minimum_spanning_tree, total_weight = prim(graph)

if len(minimum_spanning_tree) == len(graph) - 1:
    print("Minimum Spanning Tree:")
    for edge in minimum_spanning_tree:
        print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
    print(f"Total Weight of Minimum Spanning Tree: {total_weight}")
else:
    print("The input graph is not connected, so no minimum spanning tree exists.")
