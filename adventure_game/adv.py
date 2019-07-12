import sys
from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Declare all the items
boots = Item("boots", "run with lightning speed!")
flashlight = Item("flashlight", "guide your way out of the darkness.")
sword = Item("sword", "safety first!")

room["outside"].add_item(boots.name)
room["treasure"].add_item(boots.name)
room["foyer"].add_item(boots.name, flashlight.name, sword.name)
room["narrow"].add_item(flashlight.name, sword.name)
room["overlook"].add_item(flashlight.name)


# function for printing game specs
def print_game():
    print("🏠  Room: {} - {}".format(player.current_room.name, player.current_room.description))
    print("📦  Room Items: {}".format(player.current_room.items)) 
    print("🛍  Player Items: {}\n".format(player.items))

# Make a new player object that is currently in the 'outside' room and holds no items
player = Player(room["outside"])
player.take_item()
print_game()

# Wait for user input and decide what to do
command = input("Enter action: ")

while(command != "q"):
    # Print an error message for invalid action
    if not(command in ["n", "s", "w", "e", "q"] or (len(command.split()) == 2 and (command.startswith("take") or command.startswith("drop")))):
        print("❓  Please enter a valid command.\n")
    else:

        # If the user enters a cardinal direction, attempt to move to the room there
        if command in ["n", "s", "w", "e"]:
            if getattr(player.current_room, f"{command}_to"):
                player.current_room = getattr(player.current_room, f"{command}_to")
                print_game()
            else:
                print("🚫  You can't go that way.\n")

        if len(command.split()) == 2:
            verb = command.split()[0]
            item = command.split()[1]

             # If the player takes item, add to player and remove it from room
            if verb == "take":
                if item in player.current_room.items:
                    player.take_item(item)
                    player.current_room.items.remove(item)
                    print_game()
                else:
                    print("❌  This item is not in the room.\n")

            # If the player drops item, remove from player and add it to room
            if verb == "drop":
                if item in player.items:
                    player.items.remove(item)
                    player.current_room.items.append(item)
                    print_game()
                else:
                    print("❌  You don't have this item.\n")
                
    command = input("Enter action: ")

# If the user enters "q", quit the game
if command == "q":
    print("Goodbye! 👋")
    sys.exit()