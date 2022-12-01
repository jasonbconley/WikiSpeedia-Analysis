import networkx as nx
from sknetwork.data import from_graphml
from sknetwork.clustering import Louvain
import numpy as np
import pandas as  pd

graph = from_graphml("wiki_data/wiki_network.graphml")
adjacency = graph.adjacency
names = graph.names

G = nx.read_graphml("wiki_data/wiki_network.graphml")
positions = {}
positions = nx.spring_layout(G)

labels = Louvain().fit_transform(adjacency)

communities = list(zip(names, labels))
community_df = pd.DataFrame(communities, columns = ['Name', 'Community'])
community_df.to_csv("wiki_data/community_list.csv")
