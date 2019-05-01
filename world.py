class Room:

    def __init__(self, name):
        self.name = name


class Map:

    def __init__(self, name, size=5):
        self.name = name

        # must have an even perimeter so that the center can be defined
        # if even then ok
        if size % 2 > 0:
            self.size = size
        # if odd then +1 to make even
        else:
            self.size = size + 1

        # center is the center position in the array
        #   we -1 because array starts at 0, not 1
        self.center = int((self.size - 1) / 2)
        self.array = [[0] * self.size for _ in range(self.size)]

        # automatically create set rooms, for testing
        self.create_rooms()

    def create_rooms(self):
        # create first room is exact center
        self.add_room(self.center, self.center, 'Hallway')
        # make second room to the left of the center
        self.add_room(self.center - 1, self.center, 'Living Room')
        # make third room right of center
        self.add_room(self.center + 1, self.center, 'Kitchen')

        self.add_room(3, 3, 'Dining Room')

    def add_room(self, x, y, name):
        # there is no room at this location create room
        if self.array[y][x] == 0:
            self.array[y][x] = Room(name)
        # if there is a room do nothing
        else:
            print('room already exists')

    def remove_room(self, x, y):
        # remove room by setting value to 0
        self.array[y][x] = 0

    def check_map(self):
        for column in self.array:
            for row in column:
                if type(row) == Room:  # if the value is an object of type room then
                    print(row.name[0].upper(), end=' ')  # first character of string capitalized
                else:
                    print(row, end=' ')
            print()

    def check_room(self, x, y):
        return self.array[y][x].name

    def check_connected(self, x, y):
        temp = self.array

        result = []

        # check each direction to see if it within bounds of the array
        #   if it is and there is a room append result to array for returning
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

        # if at the end of this process there is nothing in the array return message
        if len(result) == 0:
            print('there are no connected rooms')

        else:
            print(result)

        return result
