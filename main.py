import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

# g is the Karate Club Graph
g = nx.karate_club_graph()
nx.draw(g)
plt.show()

# degree centrality
deg_centrality = nx.degree_centrality(g)
print(f'max degree centrality node {max(deg_centrality)} = {deg_centrality[max(deg_centrality)]}')


# Closeness Centrality
close_centrality = nx.closeness_centrality(g)

# Betweenness Centrality
bet_centrality = nx.betweenness_centrality(g, normalized=True,endpoints=False)

# Page Rank
# The value of alpha is usually set between 0.8 to 0.9.
pr = nx.pagerank(g, alpha = 0.8)


# Katz Centrality
k_centrality = nx.katz_centrality(g)


# Eigenvector Centrality
e_centrality = nx.eigenvector_centrality(g)


print(tabulate([(node,deg_centrality[node],close_centrality[node],bet_centrality[node],pr[node],k_centrality[node],e_centrality[node]) for node in e_centrality], headers=['Node','Degree Centrality', 'Closeness Centrality', 'Betweenness Centrality','Page Rank', 'Katz Centrality','Eigenvector Centrality']))
