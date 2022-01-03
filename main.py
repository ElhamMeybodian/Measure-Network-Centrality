import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

# g is the Karate Club Graph
g = nx.karate_club_graph()
nx.draw(g)
plt.show()

# degree centrality
deg_centrality = nx.degree_centrality(g)
# print(tabulate([(node,deg_centrality[node]) for node in deg_centrality], headers=['Node', 'Degree Centrality']))
# print('\n')

# Closeness Centrality
close_centrality = nx.closeness_centrality(g)
# print(tabulate([(node,close_centrality[node]) for node in close_centrality], headers=['Node', 'Closeness Centrality']))
# print('\n')

# Betweenness Centrality
bet_centrality = nx.betweenness_centrality(g, normalized=True,endpoints=False)
# print(tabulate([(node,bet_centrality[node]) for node in bet_centrality], headers=['Node', 'Betweenness Centrality']))
# print('\n')

# Page Rank
pr = nx.pagerank(g, alpha = 0.8)
# print(tabulate([(node,pr[node]) for node in pr], headers=['Node', 'Page Rank']))
# print('\n')

# Katz Centrality
k_centrality = nx.katz_centrality(g)
# print(tabulate([(node,k_centrality[node]) for node in k_centrality], headers=['Node', 'Katz Centrality']))
# print('\n')


# Eigenvector Centrality
e_centrality = nx.eigenvector_centrality(g)
# print(tabulate([(node,e_centrality[node]) for node in e_centrality], headers=['Node', 'Eigenvector Centrality']))
# print('\n')

print(tabulate([(node,deg_centrality[node],close_centrality[node],bet_centrality[node],pr[node],k_centrality[node],e_centrality[node]) for node in e_centrality], headers=['Node','Degree Centrality', 'Closeness Centrality', 'Betweenness Centrality','Page Rank', 'Katz Centrality','Eigenvector Centrality']))
