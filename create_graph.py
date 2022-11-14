import pandas as pd
import networkx as nx
import urllib as url
import unicodedata


def format_string(url_str):
    url_parse = url.parse.unquote(url_str)
    return unicodedata.normalize('NFD', url_parse).encode('ascii', 'ignore').decode("utf-8", "replace")


def get_edge_file():
    edge_file = open("wiki_data/links.tsv", "rb")
    graph = nx.read_edgelist(edge_file)
    edge_file.close()
    return graph


def read_node_file():
    nodes = pd.read_csv('wiki_data/articles.tsv')
    nodes["Article_Name"] = nodes["Article_Name"].apply(format_string)
    return nodes


def get_node_list():
    nodes = pd.read_csv('wiki_data/articles.tsv')
    nodes["Article_Name"] = nodes["Article_Name"].apply(format_string)
    return nodes["Article_Name"]


def create_graph():
    nodes = read_node_file()
    graph = get_edge_file()
    nx.set_node_attributes(graph, nodes.to_dict(), 'ArticleName')
    return graph


# Interesting problem, need to find a community of nodes that are isolated in a group of 3
def main():
    wiki_network = create_graph()

    col_names = ['src', 'dest']
    links = pd.read_csv("wiki_data/links.tsv", delimiter='\t', names=col_names)
    links["src"] = links["src"].apply(format_string)
    links["dest"] = links["dest"].apply(format_string)

    # Found these through a long an arduous programming process that resulted in me just staring at the dataset
    # Here are the three nodes that formed the disconnected community
    wiki_network.remove_node("Friend_Directdebit")
    wiki_network.remove_node("Directdebit")
    wiki_network.remove_node("Sponsorship_Directdebit")

    nx.write_gml(wiki_network, "./wiki_data/wiki_network.gml")


if __name__ == "__main__":
    main()
