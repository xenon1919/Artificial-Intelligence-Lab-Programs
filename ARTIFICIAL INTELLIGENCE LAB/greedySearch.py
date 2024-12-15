from queue import PriorityQueue

def best_first_search(graph, actual_Src, target, heuristic_values):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic_values[actual_Src], actual_Src))
    visited.add(actual_Src)

    while not pq.empty():
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            break

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                pq.put((heuristic_values[v], v))

    print()

# Define the graph
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'E': ['H'],
    'F': ['I', 'G'],
    'C': [],
    'D': [],
    'H': [],
    'I': [],
    'G': []
}

# Define heuristic values for each node
heuristic_values = {
    'S': 13,
    'A': 12,
    'B': 4,
    'C': 7,
    'D': 3,
    'E': 8,
    'F': 2,
    'H': 4,
    'I': 9,
    'G': 0
}

# Define source and target nodes
source = 'S'
target = 'G'

print("Best-First Search with Heuristic Values:")
best_first_search(graph, source, target, heuristic_values)
