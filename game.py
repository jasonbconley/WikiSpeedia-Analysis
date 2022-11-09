from time import sleep

# Placeholder functions
def getEasyGame():
    return "Ez mode", "EZ"

def getMediumGame():
    return "Time for a mid \U0001f929  game", "MID"

def getHardGame():
    return "Time for a hard \U0001fae6  game", "HARD"

def getPath():
    return "This is a path"

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

endGame = False

while (not endGame):

    level = input("Choose your difficulty! (easy (e), medium (m), hard (h): ")
    while level != 'e' and level != 'm' and level != 'h':
        print("Invalid input my dude")
        level = input("Choose your difficulty! (easy (e), medium (m), hard (h): ")


    if level == 'e':
        source, destination = getEasyGame()
    elif level == 'm':
        source, destination = getMediumGame()
    elif level == 'h':
        source, destination = getHardGame() 
    else:
        print ("how did you get here???")
        exit(2)
    
    print(source)
    print(destination)
    sleep(2)

    revealPath = input("Do you want to see the path? [y,n]: ")
    while (revealPath != 'y' and revealPath != 'n'):
        print("c'mon gimme a y or a n")
        revealPath = input("Do you want to see the path? [y,n]: ")
    
    if (revealPath == 'y'):
        print(getPath())
    elif (revealPath == 'n'):
        print("Ok tryhard....")
        sleep(2)

    goAgain = input("Do you want a new game?? [y,n]: ")
    while (goAgain != 'y' and goAgain != 'n'):
        print("y or n buddy...")
        revealPath = input("Do you want a new game?? [y,n]: ")

    if (goAgain == 'n'):
        endGame = True

print("goodbye")

