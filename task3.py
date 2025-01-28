import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

stations = [
    "Station A", "Station B", "Station C", "Station D",
    "Station E", "Station F", "Station G", "Station H"
]

graph.add_nodes_from(stations)

connections_with_weights = [
    ("Station A", "Station B", 2), ("Station B", "Station C", 3),
    ("Station C", "Station D", 1), ("Station D", "Station E", 4),
    ("Station E", "Station F", 2), ("Station F", "Station G", 3),
    ("Station G", "Station H", 1), ("Station H", "Station A", 5),
    ("Station A", "Station C", 7), ("Station E", "Station G", 2)
]

graph.add_weighted_edges_from(connections_with_weights)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(graph)
nx.draw(
    graph, pos, with_labels=True, node_color="skyblue", node_size=500,
    edge_color="gray", font_size=10, font_weight="bold"
)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.title("Транспортна мережа метро з вагами", fontsize=14)
plt.show()

def dijkstra_all_pairs(graph):
    shortest_paths = {}
    for start in graph.nodes():
        shortest_paths[start] = nx.single_source_dijkstra_path_length(graph, start)
    return shortest_paths

shortest_paths = dijkstra_all_pairs(graph)

print("Найкоротші шляхи між всіма вершинами:")
for start, paths in shortest_paths.items():
    print(f"Від {start}:")
    for end, distance in paths.items():
        print(f"  До {end}: {distance}")