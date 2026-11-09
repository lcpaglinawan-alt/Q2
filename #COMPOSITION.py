#COMPOSITION

class Room:
    def _init_ (self,name: str):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom") ]

House1 = House()
for room in House1.rooms:
    print (f"Room Created: {room.name}")

my_house = House()
for room in my_house.rooms:
    print (r"Room created: {room.name}")
