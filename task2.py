import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

graph = nx.Graph()

stations = [
    "Station A", "Station B", "Station C", "Station D",
    "Station E", "Station F", "Station G", "Station H"
]

graph.add_nodes_from(stations)

connections = [
    ("Station A", "Station B"), ("Station B", "Station C"),
    ("Station C", "Station D"), ("Station D", "Station E"),
    ("Station E", "Station F"), ("Station F", "Station G"),
    ("Station G", "Station H"), ("Station H", "Station A"),
    ("Station A", "Station C"), ("Station E", "Station G")
]

graph.add_edges_from(connections)

plt.figure(figsize=(8, 6))
nx.draw(
    graph, with_labels=True, node_color="skyblue", node_size=500,
    edge_color="gray", font_size=10, font_weight="bold"
)
plt.title("Транспортна мережа метро", fontsize=14)
plt.show()
def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None

def bfs(graph, start, end):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

start_station = "Station A"
end_station = "Station G"

dfs_path = dfs(graph, start_station, end_station)
print(f"Шлях за допомогою DFS: {dfs_path}")

bfs_path = bfs(graph, start_station, end_station)
print(f"Шлях за допомогою BFS: {bfs_path}")

print("\nПорівняння результатів:")
print(f"DFS шлях: {dfs_path}")
print(f"BFS шлях: {bfs_path}")

if dfs_path == bfs_path:
    print("Шляхи однакові.")
else:
    print("Шляхи різні.")

"""
DFS шлях: Може бути довшим, оскільки алгоритм намагається йти в глибину,
ігноруючи можливі коротші шляхи.
BFS шлях: Завжди знаходить найкоротший шлях, оскільки досліджує всі можливі шляхи по рівнях.
"""