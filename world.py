class Map:

    def __init__(self, name):
        self.name = str(name).lower().strip()
        self.rooms = []

    def add_room(self, name):
        self.rooms.append(Room(name))

    def get_room(self, number):
        return self.rooms[number]

    def get_rooms(self):
        room_list = []
        for room_ in self.rooms:
            room_list.append(room_.name)

        return room_list

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Room:

    def __init__(self, name):
        self.name = name
        self.location = None
        self.connected_rooms = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def connect_room(self, room):
        self.connected_rooms.append(room)