import networkx as nx
import matplotlib.pyplot as plt

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

num_nodes = graph.number_of_nodes()
num_edges = graph.number_of_edges()
degree_dict = dict(graph.degree())

print(f"Кількість вершин (зупинок метро): {num_nodes}")
print(f"Кількість ребер (зв'язків між зупинками): {num_edges}")
print("Ступінь вершин (кількість зв'язків для кожної зупинки):")
for station, degree in degree_dict.items():
    print(f"  {station}: {degree}")
