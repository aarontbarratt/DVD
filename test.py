from world import Room


def print_array(array):
    for column in array:
        for row in column:
            if type(row) is Room:
                print(row.name, end=' ')
            else:
                print(row, end=' ')
        print()  # prints new line


def check_connected(array, x, y):
    temp = array
    temp[y][x] = 'H'
    print_array(temp)

    result = []

    if y + 1 <= size - 1:
        if temp[y + 1][x] != 0:
            result.append(temp[y + 1][x])

    if x + 1 <= size - 1:
        if temp[y][x + 1] != 0:
            result.append(temp[y][x + 1])

    if y - 1 >= 0:
        if temp[y - 1][x] != 0:
            result.append(temp[y - 1][x])

    if x - 1 >= 0:
        if temp[y][x - 1] != 0:
            result.append(temp[y][x - 1])

    return result


size = 5
a = [[0] * size for i in range(size)]

a[0][0] = 1
a[1][0] = 2
a[0][1] = 3
a[4][4] = 5

check = check_connected(a, 2, 2)
print(check)
