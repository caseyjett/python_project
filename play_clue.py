import random 

characters = [
    "Mrs. White", 
    "Mrs. Peacock", 
    "Professor Plum", 
    "Colonel Mustard", 
    "Miss Scarlett", 
    "Mr. Green", 
]

weapons = [
    "Knife", 
    "Revolver", 
    "Rope", 
    "Wrench"
    "Candlestick", 
    "Lead pipe"
]

rooms = [
    "Billiard Room", 
    "Conservatory", 
    "Dining Hall", 
    "Kitchen", 
    "Hall", 
    "Ballroom", 
    "Lounge", 
    "Library", 
    "Study"
]

the_murder = []
def random_murder():
    murderer = random.choice(characters)
    murder_location = random.choice(rooms)
    murder_weapon = random.choice(weapons)

    the_murder.append(murderer)
    the_murder.append(murder_location)
    the_murder.append(murder_weapon)

class Player: 
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def pick_player(self):
        print("\nWhich character would you like to play as? \n")
        for idx, character in enumerate(characters):
            print(f"---{idx}) {character}")
        chosen_character = int(input("\nEnter a number: "))
        play_as = characters[chosen_character]
        print("You are now " + play_as + "\n")
        return chosen_character #So that I can access chosen_character? 
        # for character in characters:
        #     # find the chosen character and print it like "Okay Mr. Green welcome to the ... and explain rules of the game. Also remove player from the list of people that can be asked"
        #     pass

    def next_room(self):
        current = self.current_room
        print("Which room would you like to go to next? ")
        for idx, room in enumerate(current.connections):
            print(f'---{idx}) {room}')
        chosen_room = int(input("\nEnter a number: "))
        play_in = rooms[chosen_room]
        print("You are now in the " + play_in + "\n") #I would really like to be able to use the characters name here instead of "You"
        self.current_room = current.connections[chosen_room]
        

class Room:

    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_adjacent_room(self, room):
        self.connections.append(room)


def in_play():
    ballroom = Room("Ballroom")
    billiard_room = Room("Billiard Room")
    conservatory = Room("Conservatory")
    dining_hall = Room("Dining Hall")
    kitchen = Room("Kitchen")
    hall = Room("Hall")
    lounge = Room("Lounge")
    library = Room("Library")
    study = Room("study")

    ballroom.add_adjacent_room(conservatory)
    ballroom.add_adjacent_room(billiard_room)
    ballroom.add_adjacent_room(kitchen)

    billiard_room.add_adjacent_room(ballroom)
    billiard_room.add_adjacent_room(dining_hall)
    billiard_room.add_adjacent_room(library)
    billiard_room.add_adjacent_room(hall)

    conservatory.add_adjacent_room(library)
    conservatory.add_adjacent_room(ballroom)
    conservatory.add_adjacent_room(lounge)

    dining_hall.add_adjacent_room(lounge)
    dining_hall.add_adjacent_room(kitchen)
    dining_hall.add_adjacent_room(billiard_room)

    kitchen.add_adjacent_room(ballroom)
    kitchen.add_adjacent_room(dining_hall)
    kitchen.add_adjacent_room(study)

    hall.add_adjacent_room(study)
    hall.add_adjacent_room(lounge)
    hall.add_adjacent_room(billiard_room)

    lounge.add_adjacent_room(conservatory)
    lounge.add_adjacent_room(hall)
    lounge.add_adjacent_room(dining_hall)

    library.add_adjacent_room(study)
    library.add_adjacent_room(billiard_room)
    library.add_adjacent_room(conservatory)

    study.add_adjacent_room(library)
    study.add_adjacent_room(hall)
    study.add_adjacent_room(kitchen)


    player = Player("player", billiard_room)

    player.pick_player()
    player.next_room()


    # while True:
    #     # This is the big loop. 
    #     # Game
    #     # Help
    #     # Quit
    #     # Map, etc. 
    #     pass

random_murder()
# print(the_murder)

in_play()

# print("""
# X--------------------------------------------X
# |              |              |              |
# |    Study     |    Hall      |   Lounge     |
# |              |              |              |
# |--------------------------------------------|
# |              |              |              |
# |              |              |              |
# |   Library    |   Billiard   |    Dining    |
# |              |     Room     |     Hall     |
# |              |              |              |  
# |--------------------------------------------|
# |              |              |              |
# | Conservatory |   Ballroom   |    Kitchen   |
# |              |              |              |
# X--------------------------------------------X
# """)

# This is just messing around with my options when I get here... 
# def guessing():
#     if "Mrs. White" == the_murder[0]:
#         print("Wowza")
#     else: 
#         print("Not this time")
# guessing()


    

