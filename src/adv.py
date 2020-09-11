from room import Room
from items.weapon import Weapon 
from items.item import Item 
from player import Player

# Declare all the items

weapon = {
    'shield': Weapon('Shield', 'A shield that can be used to protect yourself', 20),

    'sword': Weapon('Sword', 'An ancient sword that can be used to slay your enemies', 60),
}

item = {
    
    'berries': Item('Berries', 'Magic berries that will restore your health'),

    'torch': Item('Torch', 'A wooden stick wrapped in cloth and lit on fire, helps illuminate the cave')
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['torch'], []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [], weapon['shield']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['berries'], []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['berries'], weapon['sword']),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playing = True

player = Player(input('Enter your name >> '), room['outside'], [])



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while playing:
    print(f'{player}')
    print("\n")

    print('Enter "n", "s", "e", or "w" to move North, South, East or West  \n Press "q" to quit the game')

    cmd = input(" >>> ")
    
    if cmd in ["n", "s", "e", "w"]:
        
        try:
            player.location = getattr(player.location, f'{cmd}_to')
        except AttributeError:
            print('Not a valid direction')
    
    # elif cmd == 'i':
    #     player.print_inventory()
        
    
    elif cmd == 'q':
        playing = False
        print("Thanks for playing")
    # else:
    #     print(f'{cmd} is not a valid input')
        
    elif len(cmd.split(' ')) > 1:
        action, item_name = cmd.split(' ')

        if action == 'get' or action == 'take':
            if item_name not in item or item[item_name] not in getattr(player.location, 'items'):
                print('Sorry, that item is not here anymore')

            else:
                picked_up_item = item[item_name]
                player.location.remove_item(picked_up_item)
                player.get(picked_up_item)
                picked_up_item.on_take()

        if action == 'drop':
            if item_name not in item or item[item_name] not in getattr(player, 'items'):
                print('You are not carrying that item')

            else:
                dropped_item = item[item_name]
                player.drop(dropped_item)
                player.location.store_item(dropped_item)
                dropped_item.on_drop()
            

    # if action == 'get':
    #     picked_up_item = [item_name]
    #     player.location.remove_item(picked_up_item)
    #     picked_up_weapon = [item_name]
    #     player.location.remove_weapon(picked_up_weapon)
    #     player.get(picked_up_item)
    #     player.get(picked_up_weapon)
    #     picked_up_item.on_take()
    #     picked_up_weapon.on_take()
    
    # if action == 'drop':
    #     dropped_item = item[item_name]
    #     player.drop(dropped_item)
    #     dropped_weapon = weapon[item_name]
    #     player.drop(dropped_weapon)
    #     player.location.store_item(dropped_item)
    #     player.loation.store_weapon(dropped_weapon)
    #     dropped_item.on_drop()
    #     dropped_weapon.on_drop()

