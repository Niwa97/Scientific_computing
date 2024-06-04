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
  V = list(G.nodes())
  E = list(G.edges)
  W = nx.get_edge_attributes(G, "weight")
  L = []
  P = {}
  L.append(V[0])
  index = 0
  MST = nx.Graph()
  MST.add_node(V[0])
  while(len(L) < N):
    P.update({y: W[y] for y in E if y[0]==V[index] or y[1]==V[index]})
    P = dict(sorted(P.items(), key=lambda item: item[1]))
    x = y = 0
    while(x in L and y in L):
      x,y = list(P.keys())[0]
      P.pop((x,y))
    MST.add_edge(x, y, weight = W[(x,y)])
    if(y not in L):
      index = y
      L.append(V[index])
      MST.add_node(V[index])
    else:
      index = x
      L.append(V[index])
      MST.add_node(V[index])
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
sorted(T.edges(data=True))
