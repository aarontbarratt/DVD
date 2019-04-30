from player import Player


class Map:

    def __init__(self, name):
        self.name = name
        self.size = 5
        self.array = [[0] * self.size for _ in range(self.size)]
        self.create_rooms()

    def create_rooms(self):
        self.add_room(0, 0)
        self.add_room(0, 1)
        self.add_room(1, 1)
        self.add_room(1, 2)

    def add_room(self, x, y):
        self.array[y][x] = self.get_highest_room_value() + 1

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

    def get_lowest_room_value(self):
        return min(min(x) for x in self.array)


player = Player('Aaron')
player.get_stats()

world = Map('INVU')
world.check_map()

world.check_connected(player.pos_x, player.pox_y)

# move players y_pos
player.pos_y = 1
world.check_connected(player.pos_y, player.pox_y)
