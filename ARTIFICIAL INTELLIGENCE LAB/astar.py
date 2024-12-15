from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(start, goal, graph, heuristic_values):
    open_set = PriorityQueue()
    closed_set = set()
    start_node = Node(state=start, heuristic=heuristic_values[start])
    open_set.put(start_node)

    while not open_set.empty():
        current_node = open_set.get()
        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)
        for neighbor, cost in graph[current_node.state]:
            if neighbor not in closed_set:
                heuristic = heuristic_values[neighbor]
                new_cost = current_node.cost + cost
                new_node = Node(state=neighbor, parent=current_node, cost=new_cost, heuristic=heuristic)
                open_set.put(new_node)

    return None

# Define the graph with adjacency list representation
graph = {
    'S': [('A', 0), ('B', 0)],
    'A': [('C', 0), ('D', 0)],
    'B': [('E', 0), ('F', 0)],
    'E': [('H', 0)],
    'F': [('I', 0), ('G', 0)],
    'C': [],
    'D': [],
    'H': [],
    'I': [],
    'G': []
}

# Heuristic values for each node
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

start_node = 'S'
goal_node = 'G'

path = astar(start_node, goal_node, graph, heuristic_values)

if path:
    print("Path:", path)
else:
    print("No path found.")
