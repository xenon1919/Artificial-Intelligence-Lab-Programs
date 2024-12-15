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

def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

print("Depth-First Search:")
dfs('S', [])
