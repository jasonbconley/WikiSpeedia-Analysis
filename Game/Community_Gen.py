import networkx as nx
from sknetwork.data import from_graphml
from sknetwork.clustering import Louvain
import numpy as np
import pandas as  pd

graph = from_graphml("../wiki_data/wiki_network.graphml")
adjacency = graph.adjacency
names = graph.names

G = nx.read_graphml("../wiki_data/wiki_network.graphml")

labels = Louvain().fit_transform(adjacency)

communities = list(zip(names, labels))
community_df = pd.DataFrame(communities, columns = ['Name', 'Community'])
community_df.sort_values(by = ['Community'])

# Storing community sizes
group_df = community_df.groupby(['Community']).count()

community_df.to_csv("../wiki_data/community_list.csv")

comm_0 = list(community_df[community_df['Community'] == 0]['Name'])

comm_numbers = list(community_df.Community.unique())
comm_numbers.sort()

diameters = []
for comm_num in comm_numbers:
    comm = list(community_df[community_df['Community'] == comm_num]['Name'])
    diam = nx.diameter(G.subgraph(comm))
    print("Community #{} has diameter {}".format(comm_num, diam))
    diameters.append(diam)

diam_zip = list(zip(comm_numbers, diameters))
diameter_df = pd.DataFrame(diam_zip, columns = ['Community Number', 'Diameter'])
diameter_df.sort_values(by = ['Diameter'])
diameter_df.to_csv("../wiki_data/community_diameters.csv")
