        # Name: Alice Smith (your name here!)

def show_instructions():
    print("""
Text-Based Adventure Game
=========================
Commands:
    go [direction]
    get [item]
    use [item]""")

def show_status():
    print("---------------------------")
    print("You are in the " + current_room)
    print(rooms[current_room]['description'])
    print("Inventory: " + str(inventory))
    print("---------------------------")

# Game setup
inventory = []
rooms = {
    'Hall': {
        'description': 'a long hallway with paintings on the walls.',
        'items': [],
        'actions': {
            'north': 'Kitchen',
            'east': 'Living Room'
        }
    },
    'Kitchen': {
        'description': 'a kitchen with a fridge and a table.',
        'items': ['key'],
        'actions': {
            'south': 'Hall'
        }
    },
    'Living Room': {
        'description': 'a cozy living room with a fireplace.',
        'items': [],
        'actions': {
            'west': 'Hall',
            'north': 'Garden'
        }
    },

    'Garden': {
        'description': 'a beautiful garden with blooming flowers.',
        'items': [],
        'actions': {
            'south': 'Living Room'
        }
    }
}

current_room = 'Hall'

show_instructions()

# Game loop
while True:
    show_status()

    # Get the player's next move
    move = input("> ").lower().split()

    # Check if the player wants to move
    if move[0] == 'go':
        direction = move[1]
        if direction in rooms[current_room]['actions']:
            current_room = rooms[current_room]['actions'][direction]
        else:
            print("You can't go that way.")

    # Check if the player wants to get an item
    elif move[0] == 'get':
        item = move[1]
        if item in rooms[current_room]['items']:
            inventory.append(item)
            rooms[current_room]['items'].remove(item)
            print("You picked up the " + item + ".")
        else:
           print("There is no " + item + " here.")

    # Implement more commands and game logic here

    # Example ending condition
    if current_room == 'Garden' and 'key' in inventory:
        print("You used the key to unlock the gate and escaped, you win!")
        break
