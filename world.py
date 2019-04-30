class Room:

    def __init__(self, name):
        self.name = name


class Map:

    def __init__(self, name):
        self.name = name

        self.size = 5
        self.center = int((self.size - 1) / 2)
        self.array = [[0] * self.size for _ in range(self.size)]

        self.create_rooms()

    def create_rooms(self):
        self.add_room(self.center, self.center, 'Hallway')
        self.add_room(self.center - 1, self.center, 'Living Room')
        self.add_room(self.center + 1, self.center, 'Kitchen')
        self.add_room(3, 3, 'Dining Room')

    def add_room(self, x, y, name):
        if self.array[y][x] == 0:
            self.array[y][x] = Room(name)
        else:
            print('room already exists')

    def remove_room(self, x, y):
        self.array[y][x] = 0

    def check_map(self):
        for column in self.array:
            for row in column:
                if type(row) == Room:
                    print(row.name[0].upper(), end=' ')
                else:
                    print(row, end=' ')
            print()

    def check_room(self, x, y):
        return self.array[y][x].name

    def check_connected(self, x, y):
        temp = self.array

        result = []

        if y + 1 <= self.size - 1:
            if temp[y + 1][x] != 0:
                result.append(temp[y + 1][x].name)

        if x + 1 <= self.size - 1:
            if temp[y][x + 1] != 0:
                result.append(temp[y][x + 1].name)

        if y - 1 >= 0:
            if temp[y - 1][x] != 0:
                result.append(temp[y - 1][x].name)

        if x - 1 >= 0:
            if temp[y][x - 1] != 0:
                result.append(temp[y][x - 1].name)

        if len(result) == 0:
            print('there are no connected rooms')
        else:
            print(result)
        return result
