from time import sleep
from networkx import read_graphml
from networkx import dijkstra_path
from pandas import read_csv
from random import choice

def load_graph_data():
    graph = read_graphml("../wiki_data/wiki_network.graphml")
    node_communities = read_csv("../wiki_data/community_list.csv")
    return graph, node_communities

def get_easy_game(graph, community_list):
    # The only easy community is community 1
    print("We goin Ez mode")

    # Iterate until a path of length 2 or more is found
    good_path = False
    while not good_path:
        source, dest = get_nodes(community_list, [1])
        path = dijkstra_path(graph, source, dest)
        if len(path) > 2:
            good_path = True

    return source, dest, path

def get_medium_game(graph, community_list):
    medium_communities = [0, 2, 3, 4, 5]
    print("Time for a mid \U0001f929  game")

    good_path = False
    while not good_path:
        source, dest = get_nodes(community_list, medium_communities)
        path = dijkstra_path(graph, source, dest)
        if len(path) > 2:
            good_path = True

    return source, dest, path


def get_hard_game(graph, community_list):
    # The only hard community is community 6
    print("Time for a hard \U0001fae6  game")

    good_path = False
    while not good_path:
        source, dest = get_nodes(community_list, [6])
        path = dijkstra_path(graph, source, dest)
        if len(path) > 2:
            good_path = True

    return source, dest, path

# This function finds two random nodes in the network
def get_nodes(community_list, search_communities):
    source = choice(list(community_list[community_list['Community'].isin(search_communities)]['Name']))
    dest = choice(list(community_list[community_list['Community'].isin(search_communities)]['Name']))
    while source == dest:
        dest = choice(community_list[community_list['Community'].isin(search_communities)]['Name'])
    return source, dest

def main():
    print(
        """                                         
      ----------------------------------------    
    < Welcome to Wikispeedia Game Generator!!! >   
      ----------------------------------------    
            \   ^__^                            
             \  (oo)\_______                    
                (__)\       )\/\                
                    ||----w |                   
                    ||     ||                   
    """)

    graph_data, community_list = load_graph_data()

    end_game = False

    while not end_game:

        level = input("Choose your difficulty! (easy (e), medium (m), hard (h): ")
        while level != 'e' and level != 'm' and level != 'h':
            print("Invalid input my dude")
            level = input("Choose your difficulty! (easy (e), medium (m), hard (h): ")

        if level == 'e':
            source, dest, path = get_easy_game(graph_data, community_list)
        elif level == 'm':
            source, dest, path = get_medium_game(graph_data, community_list)
        elif level == 'h':
            source, dest, path = get_hard_game(graph_data, community_list)
        else:
            print("how did you get here???")
            exit(2)

        print("The starting article is {}, and the target is {}".format(source, dest))
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        print("GO!!!")
        sleep(4)

        # Hint code, only give a hint 
        hint_level = 1
        while hint_level < len(path):
            hint = input("Do you want a hint? (articles are revealed one at a time) [y,n]: ")
            while (hint != 'y' and hint != 'n'):
                print("Give me a 'y' or 'n'")
                hint = input("Do you want a hint? [y,n]: ")
            
            if hint_level == len(path) - 1 and hint == 'y':
                print("You're very close to the end..")
            elif hint == 'y':
                print("The next article in the path is {}".format(path[hint_level]))
            elif hint == 'n':
                break

            hint_level += 1
        

        reveal_path = input("Do you want to see the path? [y,n]: ")
        while (reveal_path != 'y' and reveal_path != 'n'):
            print("Give me a 'y' or a 'n'")
            reveal_path = input("Do you want to see the path? [y,n]: ")

        if (reveal_path == 'y'):
            print([node for node in path])
        elif (reveal_path == 'n'):
            print("Are you sure your path was the shortest?")
            sleep(2)

        go_again = input("Do you want a new game?? [y,n]: ")
        while go_again != 'y' and go_again != 'n':
            print("y or n buddy...")
            go_again = input("Do you want a new game?? [y,n]: ")

        if go_again == 'n':
            end_game = True

    print("see ya")


if __name__ == "__main__":
    main()
