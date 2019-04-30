from player import Player


class Map:

    def __init__(self, name):
        self.name = name
        self.size = 5
        self.array = [[0] * self.size for _ in range(self.size)]
        self.create_rooms()

    def create_rooms(self):
        self.array[0][0] = self.get_highest_room_value() + 1
        self.array[1][0] = self.get_highest_room_value() + 1
        self.array[0][1] = self.get_highest_room_value() + 1
        self.array[4][4] = self.get_highest_room_value() + 1

    def add_room(self, x, y):
        self.array[y][x] = 999

    def remove_room(self, x, y):
        self.array[y][x] = 0

    def check_map(self):
        for column in self.array:
            for row in column:
                print(row, end=' ')
            print()  # prints new line

    def check_connected(self, x, y):
        temp = self.array

        result = []

        if y + 1 <= self.size - 1:
            if temp[y + 1][x] != 0:
                result.append(temp[y + 1][x])

        if x + 1 <= self.size - 1:
            if temp[y][x + 1] != 0:
                result.append(temp[y][x + 1])

        if y - 1 >= 0:
            if temp[y - 1][x] != 0:
                result.append(temp[y - 1][x])

        if x - 1 >= 0:
            if temp[y][x - 1] != 0:
                result.append(temp[y][x - 1])

        print(result)
        return result

    def get_highest_room_value(self):
        return max(max(x) for x in self.array)


aaron = Player('Aaron')
stats = aaron.get_stats()
print(stats)

house = Map('Lair')
house.check_map()
house.check_connected(aaron.pos_x, aaron.pos_x)