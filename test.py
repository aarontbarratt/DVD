from world import Room


def print_array(array):
    for row in array:
        for column in row:
            if type(column) is Room:
                print(column.name, end=' ')
            else:
                print(column, end=' ')
        print()  # prints new line


size = 5
a = [[0] * size for i in range(size)]

living_room = Room('Living Room')

a[4][2] = 1
a[3][2] = 2
a[2][2] = 3
a[2][1] = 4
a[2][0] = 5
a[1][0] = 6
a[2][3] = 7
print_array(a)
