import networkx as nx
import matplotlib.pyplot as plt

G = {
    '0': ['1', '2', '3'],
    '1': ['3'],
    '2': ['0', '3'],
    '3': ['0', '1', '2', '4'],
    '4': ['3'],
}

print(G)

# Visualización del grafo
G_visualizacion = nx.from_dict_of_lists(G)
start_vertex = '0'

# Dibujar el grafo
nx.draw(G_visualizacion, with_labels=True, node_color='lightblue', node_size=1000, font_size=10)
plt.title('DFS Transversal Path from Vertex ' + start_vertex)
plt.show()

def dfs_iter(G, v, marked):
    stack = [v]
    path = []

    while stack:
        v = stack.pop()
        if not marked[v]:
            marked[v] = True
            path.append(v)
            for w in G[v]:
                if not marked[w]:
                    stack.append(w)
    return path


