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


def create_graph():
    nodes = read_node_file()
    graph = get_edge_file()
    nx.set_node_attributes(graph, nodes.to_dict(), 'ArticleName')
    return graph


def main():
    wiki_network = create_graph()

    print(wiki_network.number_of_edges())

    nx.write_gml(wiki_network, "./wiki_data/wiki_network.gml")


if __name__ == "__main__":
    main()
