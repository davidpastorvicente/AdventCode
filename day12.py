"""Day 12 of 2020 Advent of Code"""

file = open('./input12.txt')
text = file.read()

lines = text.split('\n')
directions = list(map(lambda x: [x[0], int(x[1:])], lines))
dict_dirs = {'S': 'N', 'W': 'E', 'R': 'L'}


def simplify_dir(direction):
    if direction[0] in dict_dirs.keys():
        direction[0] = dict_dirs[direction[0]]
        direction[1] = -direction[1]
    return direction


directions = list(map(simplify_dir, directions))


# First problem

def forward(steps, n, e):
    if angle == 0:
        e += steps
    elif angle == 90:
        n += steps
    elif angle == 180:
        e -= steps
    else:
        n -= steps

    return n, e


north, east, angle = 0, 0, 0
for i in directions:
    if i[0] == 'N':
        north += i[1]
    elif i[0] == 'E':
        east += i[1]
    elif i[0] == 'L':
        angle = (angle + i[1]) % 360
    elif i[0] == 'F':
        north, east = forward(i[1], north, east)

print(abs(north) + abs(east))


# Second problem

def rotate(degrees, n, e):
    if degrees == 90:
        return e, -n
    elif degrees == 180:
        return -n, -e
    else:
        return -e, n


w_north, w_east = 1, 10
north, east = 0, 0
for i in directions:
    if i[0] == 'N':
        w_north += i[1]
    elif i[0] == 'E':
        w_east += i[1]
    elif i[0] == 'L':
        w_north, w_east = rotate(i[1] % 360, w_north, w_east)
    elif i[0] == 'F':
        north += i[1] * w_north
        east += i[1] * w_east

print(abs(north) + abs(east))
