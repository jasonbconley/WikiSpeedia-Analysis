from time import sleep


# Placeholder functions
def get_easy_game():
    return "Ez mode", "EZ"


def get_medium_game():
    return "Time for a mid \U0001f929  game", "MID"


def get_hard_game():
    return "Time for a hard \U0001fae6  game", "HARD"


def get_path():
    return "This is a path"


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

    end_game = False

    while not end_game:

        level = input("Choose your difficulty! (easy (e), medium (m), hard (h): ")
        while level != 'e' and level != 'm' and level != 'h':
            print("Invalid input my dude")
            level = input("Choose your difficulty! (easy (e), medium (m), hard (h): ")

        if level == 'e':
            source, destination = get_easy_game()
        elif level == 'm':
            source, destination = get_medium_game()
        elif level == 'h':
            source, destination = get_hard_game()
        else:
            print("how did you get here???")
            exit(2)

        print(source)
        print(destination)
        sleep(2)

        reveal_path = input("Do you want to see the path? [y,n]: ")
        while (reveal_path != 'y' and reveal_path != 'n'):
            print("c'mon gimme a y or a n")
            reveal_path = input("Do you want to see the path? [y,n]: ")

        if (reveal_path == 'y'):
            print(get_path())
        elif (reveal_path == 'n'):
            print("Ok tryhard....")
            sleep(2)

        go_again = input("Do you want a new game?? [y,n]: ")
        while go_again != 'y' and go_again != 'n':
            print("y or n buddy...")
            reveal_path = input("Do you want a new game?? [y,n]: ")

        if go_again == 'n':
            end_game = True

    print("goodbye")


if __name__ == "__main__":
    main()
