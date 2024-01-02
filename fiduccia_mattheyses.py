import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def initial_partition(graph, k):
    subsets = [[] for _ in range(k)]
    vertices = list(graph.nodes())
    random.shuffle(vertices)
    for i, vertex in enumerate(vertices):
        subsets[i % k].append(vertex)
    return subsets

def compute_gain(graph, vertex, current_subset, other_subset):
    gain = 0
    for neighbor in graph.neighbors(vertex):
        if neighbor in current_subset: gain -= 1
        if neighbor in other_subset: gain += 1
    return gain

def fiduccia_mattheyses(graph, k, max_iterations=100):
    current_partition = initial_partition(graph, k)

    for _ in range(max_iterations):
        moved = False

        for subset_index, current_subset in enumerate(current_partition):
            for vertex in current_subset:
                gains = [compute_gain(graph, vertex, current_subset, other_subset)
                         for other_subset in current_partition if other_subset != current_subset]
                max_gain_subset = max(range(len(gains)), key=lambda i: gains[i])
                if gains[max_gain_subset] > 0:
                    current_partition[subset_index].remove(vertex)
                    current_partition[max_gain_subset].append(vertex)
                    moved = True
                    yield current_partition
        if not moved: break

G = nx.complete_graph(10)
k = 3
pos = nx.spring_layout(G)  

fig, ax = plt.subplots()
ax.set_title('Fiduccia-Mattheyses Algorithm Animation')

def update(partition):
    ax.clear()
    ax.set_title('Fiduccia-Mattheyses Algorithm Animation')
    colors = ['blue', 'green', 'yellow']
    for i, subset in enumerate(partition):
        nx.draw_networkx_nodes(G, pos, nodelist=subset, node_color=colors[i])
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

ani = animation.FuncAnimation(fig, 
                              update, 
                              frames=fiduccia_mattheyses(G, k), 
                              blit=False, 
                              interval=1000,
                              repeat=False, 
                              save_count=1000)

file_format = 'gif'
filename = 'fiduccia_mattheyses_animation.' + file_format

ani.save(filename, writer='imagemagick', fps=1)

plt.show()
