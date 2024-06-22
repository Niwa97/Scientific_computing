import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def graph_creation(N):
  G = nx.Graph()
  rng = np.random.default_rng()
  for i in range(N):
    G.add_node(i)
    for j in range(i+1,N):
      p = rng.random()
      G.add_edge(i, j, weight=round(p,2))
  return G

def prim(G):
  N = G.number_of_nodes()
  weights = nx.get_edge_attributes(G, "weight")
  accessible_edges_weights = {}
  index = 0
  MST = nx.Graph()
  MST.add_node(index)
  while(MST.number_of_nodes() < N):
    neighbors = [(min(u, v), max(u, v)) for u, v in G.edges(index)]
    accessible_edges_weights.update({y: weights[y] for y in neighbors})
    x = y = 0
    while(MST.has_node(x) and MST.has_node(y)):
      x,y = min(accessible_edges_weights, key=accessible_edges_weights.get)
      accessible_edges_weights.pop((x,y))
    if(not(MST.has_node(y))):
      index = y
    else:
      index = x
    MST.add_edge(x, y, weight = weights[(x,y)])
  return MST

G = graph_creation(6)
H = prim(G)

plt.figure(1)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
G_e = [(u, v) for (u, v, d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, edgelist=G_e)
nx.draw_networkx_labels(G, pos)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.figure(2)
pos2 = nx.spring_layout(H)
nx.draw_networkx_nodes(H, pos2)
H_e = [(u, v) for (u, v, d) in H.edges(data=True)]
nx.draw_networkx_edges(H, pos2, edgelist=H_e)
nx.draw_networkx_labels(H, pos2)
edge_labels_2 = nx.get_edge_attributes(H, "weight")
nx.draw_networkx_edge_labels(H, pos2, edge_labels_2)

plt.show()

T = nx.minimum_spanning_tree(G, algorithm='prim')
print(sorted(T.edges(data=True)))
print(nx.utils.graphs_equal(H, T))
