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

def bfs(start_node):
    visited = []
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

print("Breadth-First Search:")
bfs('S')
