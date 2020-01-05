from Player import Player

player_1 = Player()
player_2 = Player()


def start_screen():
    print("")
    print("BATTLESHIPS")
    print("Type 1: Start Local Game")
    print("Type 2: Read Instructions")
    start_screen_manager()


def start_screen_manager():
    try:
        option = int(input("Choose: "))
        if option == 1:
            print("Starting the Game...")
        elif option == 2:
            instructions()
        else:
            start_screen_manager()
    except ValueError:
        start_screen_manager()


def instructions():
    print("HOW TO PLAY BATTLESHIPS")
    print("")
    print("There are 2 players needed to play Battleships. Each player\n"
          + "starts with 5 different ships which are plotted on a 10 x 10 grid\n"
          + "Once all the ships have been plotted, each player calls coordinates\n"
          + "to try to hit the opposing player's battleships. If the player\n"
          + "fails to hit his opponent, then the coordinate will be recorded on the player's map\n"
          + "If a player was successful and hits a boat, then the screen will print that a\n"
          + "boat has been hit. If a boat sinks, then the screen will print:\n"
          + "'You Sunk My Battleship'. Once a player sinks all of the opposing ships\n"
          + "the game ends and the player that sunk all the ships is the winner.")
    print("")
    instruction_manager()


def instruction_manager():
    try:
        option = input("Press the Enter key to go back: ")
        if option == "":
            start_screen()
        else:
            instruction_manager()
    except ValueError:
        instruction_manager()




# Carrier, which has five holes.
# Battleship, which has four holes.
# Cruiser, which has three holes.
# Submarine, which has three holes.
# Destroyer, which has two holes.
class Main:
    def __init__(self):
        start_screen()


start = Main()
