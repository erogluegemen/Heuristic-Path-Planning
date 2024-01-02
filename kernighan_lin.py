import networkx as nx

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initial_partition(graph:nx.classes.graph.Graph, k:int) -> dict:
    '''
    This function initializes a partition of the graph into k subsets. 
    It assigns each vertex to a subset using modular arithmetic.

    Input: [Graph, int]
    Output: [dict]
    Sample Output: {1: 0, 2: 1, 3: 2, 4: 0, 5: 1, 6: 2}
    '''
    vertices = list(graph.nodes())
    partition = {v: i % k for i, v in enumerate(vertices)}
    return partition

def compute_gain(graph:nx.classes.graph.Graph, partition:dict, vertex:int, current_subset:int) -> int:
    '''
    This function calculates the gain of moving a vertex to a different subset.
    The gain is based on the difference in the number of neighbors in the current subset and other subsets.

    Input: [Graph, dict, int, int]
    Output: [int]
    Sample Output: 1
    '''
    gain = 0
    for neighbor in graph.neighbors(vertex):
        if partition[neighbor] != current_subset: gain += 1
        else: gain -= 1
    return gain

def plot_partition(graph:nx.classes.graph.Graph, partition:dict, ax:matplotlib.axes._axes.Axes) -> None:
    '''
    This function plots the current partition of the graph.

    Input: [Graph, dict, Axes]
    Output: [None]
    Sample Output: None
    '''
    pos = nx.spring_layout(graph)
    colors = [partition[node] for node in graph.nodes()]
    nx.draw(graph, 
            pos, 
            ax=ax, 
            node_color=colors, 
            with_labels=True)

def animate(frame:int, G:nx.classes.graph.Graph, k:int, ax:matplotlib.axes._axes.Axes) -> None:
    '''
    It performs local search iterations by moving vertices between subsets to reduce the cut size.
    The result is visualized through animation.

    Input: [int, Graph, int, Axes]
    Output: [None]
    Sample Output: None
    '''
    current_partition = initial_partition(G, k)
    cut_size = nx.cut_size(G, current_partition, weight='weight')

    for _ in range(frame):
        max_gain = 0
        move_vertex = None

        for vertex in G.nodes():
            for subset in range(k):
                gain = compute_gain(G, current_partition, vertex, subset)
                if gain > max_gain:
                    max_gain = gain
                    move_vertex = vertex
                    target_subset = subset

        if max_gain > 0:
            current_partition[move_vertex] = target_subset
            cut_size -= max_gain

    ax.clear()
    plot_partition(G, current_partition, ax)
    ax.set_title(f'Iteration {frame+1}')


if __name__ == "__main__":
    G = nx.Graph()

    # Test - 1:
    # G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1, 3), (3, 5)])

    # Test - 2:
    G.add_edges_from([(1,2), (2,3), (2,4), (4,5), (4,6), (5,6)])
    k = 2

    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, 
                                  animate, 
                                  frames=10, 
                                  fargs=(G, k, ax), 
                                  interval=1000, 
                                  repeat=False)
    file_format = 'gif'
    filename = 'graph_partition_animation.' + file_format

    ani.save(filename, writer='imagemagick', fps=1)
    plt.show()